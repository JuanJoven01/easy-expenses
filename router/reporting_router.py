from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from datetime import datetime

from services.reporter_services import get_all_expenses, get_expenses_per_category

from middlewares.auth import JWTBearer

reporter_router = APIRouter()

@reporter_router.get('/reporter/all_expenses', tags=['reporter'], dependencies=[Depends(JWTBearer())])
def all_expenses(initial_date: datetime, final_date: datetime, jwt_payload = Depends(JWTBearer())):
    try:
        user_id = jwt_payload['user_id']
        expenses = get_all_expenses(user_id= user_id, initial_date=initial_date, final_date=final_date)
        return JSONResponse(status_code=200, content=expenses)
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})
    
@reporter_router.get('/reporter/expenses_per_category', tags=['reporter'], dependencies=[Depends(JWTBearer())])
def expenses_per_category(initial_date: datetime, final_date: datetime, jwt_payload = Depends(JWTBearer())):
    try:
        user_id = jwt_payload['user_id']
        expenses = get_expenses_per_category(user_id= user_id, initial_date=initial_date, final_date=final_date)
        return JSONResponse(status_code=200, content=expenses)
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})