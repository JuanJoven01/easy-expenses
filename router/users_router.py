from fastapi import APIRouter

users_router = APIRouter()

@users_router.get('/users', tags=['users'])
def return_user():
    return {'user': 'starting'}