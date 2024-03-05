from fastapi import FastAPI
from db.config import engine, Base

from db.models import Users, Expenses, Categories

from router.users_router import users_router

app = FastAPI()

app.include_router(users_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

