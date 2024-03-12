from fastapi import FastAPI
from db.config import engine, Base

from db.models import Users, Expenses, Categories

from middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware # middleware cors

from router.users_router import users_router
from router.categories_router import categories_router
from router.expenses_router import expenses_router
from router.reporting_router import reporter_router

from middlewares.api_key import check_api_key, host

app = FastAPI()

app.add_middleware(ErrorHandler)
app.middleware("http")(check_api_key)
origins = [
    "http://localhost:5173",
    host
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(categories_router)
app.include_router(expenses_router)
app.include_router(reporter_router)

Base.metadata.create_all(bind=engine)



@app.get("/")
def read_root():
    return {"Hello": "World"}

