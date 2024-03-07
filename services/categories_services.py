from sqlalchemy import select
from db.models import Categories
from db.config import Session
from fastapi.responses import JSONResponse


def get_my_categories(user_id:int):
    '''
    Get all the categories from a specific user
    '''
    with Session() as session:
        query = select(Categories).where(Categories.user_id == user_id)
        categories = [dict(id=category.id, name= category.name, user_id=category.user_id) for category in session.execute(query).scalars().all()]
    return categories


def new_category(user_id:int, category_name:str):
    '''
    Create a new category linked with a user
    '''
    with Session() as session:
        new_category = Categories(name= category_name, user_id=user_id)
        session.add(new_category)
        session.commit()
    return True

    
def delete_category(user_id:int, category_id:int):
    '''
    remove a category linked with a user, removes too the expenses related to
    the category
    '''
    with Session() as session:
        query = select(Categories).where(Categories.id == category_id)
        category = session.execute(query).scalar()
        if category.user_id == user_id:
            session.delete(category)
            session.commit()
            return True
        else: 
            return JSONResponse(status_code=401, content={'error':'category dont belong to user'})
