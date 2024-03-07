from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from datetime import datetime

from services.expenses_services import get_my_expenses, create_new_expense

from schemas.expenses_schemas import Expense

from middlewares.auth import JWTBearer

expenses_router = APIRouter()

@expenses_router.get('/expenses/get', tags=['expenses'], dependencies=[Depends(JWTBearer())])
def get_categories(jwt_payload = Depends(JWTBearer())):
    try:
        user_id = jwt_payload['user_id']
        expenses = get_my_expenses(user_id)
        return JSONResponse(status_code=200, content=expenses)
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})
    
@expenses_router.post('/expenses/new',tags=['expenses'], dependencies=[Depends(JWTBearer())])
def new(expense:Expense, jwt_payload = Depends(JWTBearer())):
    try:
        user_id = jwt_payload['user_id']
        if not expense.date:
            expense.date = datetime.now()
        its_created = create_new_expense(name=expense.name,description=expense.description, amount=expense.amount,date=expense.date,category_id=expense.category_id,user_id=user_id)
        if its_created  == True:
            return JSONResponse(status_code=200, content={'message': 'expense created'})
        else:
            return JSONResponse(status_code=401, content=its_created)
        
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})
    