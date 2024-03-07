from sqlalchemy import select
from db.models import Expenses
from db.config import Session
from fastapi.responses import JSONResponse
import json

from services.categories_services import get_my_categories


def get_my_expenses(user_id:int):
    '''
    Get all the expenses from a specific user
    '''
    with Session() as session:
        query = select(Expenses).where(Expenses.user_id == user_id)
        expenses = [dict(id=expense.id, name= expense.name, description=expense.description, amount= expense.amount, date = expense.date, user_id=expense.user_id, category_id=expense.category_id) for expense in session.scalars(query)]
    return expenses
    
def create_new_expense(name:str, description:str, amount:float, date:str, user_id:int, category_id:int):
    '''
    Create a new expense related to an user and category
    '''
    if __verify_if_category_belong_user(user_id=user_id, category_id=category_id) == False:
        return {'error':'invalid request, category dont belong to user'}
    with Session() as session:
        new_expense = Expenses(name=name, description=description,amount=amount,date=date,user_id=user_id,category_id=category_id)
        session.add(new_expense)
        session.commit()
    return True

    
def __verify_if_category_belong_user(user_id:int, category_id:int):
    '''
    Auxiliary function to evite create a expense in a category of another user
    '''
    categories = get_my_categories(user_id=user_id)
    for category in categories:
        if category['id'] == category_id:
            return True
    return False
