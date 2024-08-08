from sqlalchemy import select
from db.models import Expenses, Categories
from db.config import Session
from fastapi.responses import JSONResponse

from datetime import timedelta


def get_all_expenses(user_id:int, initial_date:str, final_date:str):
    '''
    Get all the expenses from a specific user,
    filtered by date
    '''
    final_date = final_date + timedelta(days=1)
    with Session() as session:
        query = (
            select(Expenses)
            .where(Expenses.user_id == user_id)
            .where(Expenses.date >= initial_date)
            .where(Expenses.date <= final_date)
                 )
        expenses = [dict(id=expense.id, name=expense.name, description=expense.description, amount= expense.amount, date=str(expense.date), user_id=expense.user_id, category_id=expense.category_id) for expense in session.execute(query).scalars().all()]
    return expenses

def get_expenses_per_category(user_id:int, initial_date:str, final_date:str):
    '''
    Get all the expenses from a specific user,
    filtered by date, grouped by category
    '''
    final_date = final_date + timedelta(days=1)
    with Session() as session:
        query = (
            select(Categories.name, Expenses)
            .join(Expenses, Categories.id == Expenses.category_id)
            .where(Expenses.user_id == user_id)
            .where(Expenses.date >= initial_date)
            .where(Expenses.date <= final_date)
            .order_by(Categories.name, Expenses.date)
        )
        grouped_expenses = {}
        for row in session.execute(query):
            category_name = row[0]
            expense = row[1]
            if category_name not in grouped_expenses:
                grouped_expenses[category_name] = []
            grouped_expenses[category_name].append({
                "id": expense.id,
                "name": expense.name,
                "description": expense.description,
                "amount": expense.amount,
                "date": str(expense.date),
                "user_id": expense.user_id,
                "category_id": expense.category_id
            })
    return grouped_expenses