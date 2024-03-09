from sqlalchemy import select
from db.models import Expenses
from db.config import Session
from fastapi.responses import JSONResponse


def get_all_expenses(user_id:int, initial_date:str, final_date:str):
    '''
    Get all the expenses from a specific user,
    filtered by date
    '''
    with Session() as session:
        query = select(Expenses).where(Expenses.user_id == user_id)
        expenses = [dict(id=expense.id, name=expense.name, description=expense.description, amount= expense.amount, date=str(expense.date), user_id=expense.user_id, category_id=expense.category_id) for expense in session.execute(query).scalars().all()]
    return expenses