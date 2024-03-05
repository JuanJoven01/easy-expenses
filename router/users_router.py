from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services.users_services import create_new_user, user_login

from schemas.users_schemas import User

users_router = APIRouter()

@users_router.post('/signup', tags =['users'])
def new_user(user: User):
    try:
        username = user.username
        password = user.password
        return create_new_user(username=username, password=password)
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})
    
@users_router.post('/login', tags=['users'])
def login(user: User):
    try:
        username = user.username
        password = user.password
        return user_login(username=username, password=password)
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})