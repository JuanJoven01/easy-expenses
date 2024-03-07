from fastapi import FastAPI
from db.config import engine, Base

from db.models import Users, Expenses, Categories

from middlewares.error_handler import ErrorHandler

from router.users_router import users_router
from router.categories_router import categories_router

app = FastAPI()

app.add_middleware(ErrorHandler)

app.include_router(users_router)
app.include_router(categories_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

