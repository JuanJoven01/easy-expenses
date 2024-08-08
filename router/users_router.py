from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from services.users_services import create_new_user, user_login, change_password

from schemas.users_schemas import User, UserNewPass

from middlewares.auth import JWTBearer

users_router = APIRouter()

@users_router.post('/user/signup', tags =['users'])
def new_user(user: User):
    try:
        username = user.username
        password = user.password
        its_created = create_new_user(username=username, password=password)
        if its_created == True:
            return JSONResponse(status_code=201, content={'successful': 'User Created'})
        else:
            return its_created
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})
    
@users_router.post('/user/login', tags=['users'])
def login(user: User):
    try:
        username = user.username
        password = user.password
        token = user_login(username=username, password=password)
        return JSONResponse(status_code=200, content=token)
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})

@users_router.patch('/user/change_pass', tags=['users'], dependencies=[Depends(JWTBearer())])
def change_pass(user: UserNewPass, jwt_payload = Depends(JWTBearer())):
    try:
        username = jwt_payload['username']
        password = user.password
        new_password = user.new_password
        if change_password(username=username, password=password, new_password=new_password) == True:
            return JSONResponse(status_code=201, content={'successful': 'Password Updated'})
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})