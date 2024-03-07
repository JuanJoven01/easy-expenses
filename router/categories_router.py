from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from services.categories_services import get_my_categories, new_category, delete_category

from schemas.categories_schemas import Category

from middlewares.auth import JWTBearer

categories_router = APIRouter()

@categories_router.get('/categories', tags=['categories'], dependencies=[Depends(JWTBearer())])
def get_categories(jwt_payload = Depends(JWTBearer())):
    try:
        user_id = jwt_payload['user_id']
        return get_my_categories(user_id=user_id)
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})
    
@categories_router.post('/categories/new', tags=['categories'], dependencies=[Depends(JWTBearer())])
def new(category:Category, jwt_token = Depends(JWTBearer())):
    try:
        user_id = jwt_token['user_id']
        return new_category(user_id=user_id, category_name=category.name)
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})
    
@categories_router.delete('/categories/delete/{category_id}', tags=['categories'], dependencies=[Depends(JWTBearer())])
def delete(category_id:int, jwt_token = Depends(JWTBearer())):
    try:
        user_id = jwt_token['user_id']
        return delete_category(user_id=user_id, category_id=category_id)
    except Exception as e:
        return JSONResponse(status_code=500, content={'router error': str(e)})