from sqlalchemy import select
from passlib.context import CryptContext
from db.models import Users, Categories
from db.config import Session
from fastapi.responses import JSONResponse
from middlewares.auth import get_jwt_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def __find_user_by_name(username: str):
    '''
    Uses a query to obtain an user
    '''
    with Session() as session:
        user = session.query(Users).filter_by(username=username).first()
        if user is None:
            return False
        return user

def __hash_password(password: str):
    '''
    Just return a hashed password
    '''
    return pwd_context.hash(password)

def __verify_and_rehash_password(plain_password: str, hashed_password: str):
    '''
    Just verify if the password match an if need rehash,
    return two booleans
    '''
    password_matches = pwd_context.verify(plain_password, hashed_password)
    password_needs_rehash = pwd_context.needs_update(hashed_password)
    return password_matches, password_needs_rehash

def __check_password_and_rehash_if_needed(username: str, plain_password: str):
    '''
    Get the user and verify if need rehash the password, 
    if password is right return True and user id
    '''
    with Session() as session:
        user = __find_user_by_name(username)
        if not user:
            return False
        password_matches, password_needs_rehash = __verify_and_rehash_password(plain_password, user.password)
        if password_matches and password_needs_rehash:
            user.password = __hash_password(plain_password)
            session.commit()
        return password_matches, user.id


def create_new_user(username:str, password:str):
    '''
    First verify if id db exist an User with this username, 
    if not, create the user un db with the hashed password
    '''
    try:
        if __find_user_by_name(username=username) : return JSONResponse(status_code=400, content={'service error': 'try a new username'})
        hashed_password = __hash_password(password=password)
        with Session() as session:
            new_user = Users(username=username, password = hashed_password)
            session.add(new_user)
            session.commit()
        __create_default_categories_new_user(username=username)
        return JSONResponse(status_code=201, content={'successful': 'User Created'})
    except Exception as e:
        return JSONResponse(status_code=500, content={'service error': str(e)})

def user_login(username:str, password:str):
    '''
    Verify if username exist, then if password match, 
    '''
    try:
        user = __find_user_by_name(username=username)
        if user == False: return JSONResponse(status_code=400, content={'error': 'invalid username'})
        password_matches, user_id = __check_password_and_rehash_if_needed(username=username, plain_password=password)
        if password_matches == False: return JSONResponse(status_code=400, content={'error': 'invalid password'})
        token = get_jwt_token(user_validated=password_matches, username=username, user_id=user_id)
        return token
    except Exception as e:
        return JSONResponse(status_code=500, content={'service error': str(e)})

def change_password(username:str, password:str, new_password:str):
    '''
    First verify if id db exist an User with this username, 
    if not, call the user un db and update the pass for the new hashed
    '''
    try:
        hashed_password = __hash_password(password=new_password)
        password_matches, user_id = __check_password_and_rehash_if_needed(username=username, plain_password=password)
        if password_matches == False: return JSONResponse(status_code=400, content={'error': 'invalid password'})
        with Session() as session:
            query = select(Users).where(Users.id == user_id)
            user = session.execute(query).scalar_one()
            user.password = hashed_password
            session.commit()
        return JSONResponse(status_code=201, content={'successful': 'Password Updated'})
    except Exception as e:
        return JSONResponse(status_code=500, content={'service error': str(e)})
    
def __create_default_categories_new_user(username:str):
    try:
        user = __find_user_by_name(username=username)
        user_id = user.id
        default_categories = [
            "Food",
            "Transportation",
            "Housing",
            "Health",
            "Education",
            "Entertainment",
            "Clothing and Accessories",
            "Savings and Investment",
            "Personal Care",
            "Pets",
            "Travel and Vacation",
            "Education",
            'Governmental',
            'Others'
        ]
        with Session() as session:
            for category in default_categories:
                new_category = Categories(name=category, user_id= user_id)
                session.add(new_category)
            session.commit()
    except Exception as e:
        return JSONResponse(status_code=500, content={'service error': str(e)})