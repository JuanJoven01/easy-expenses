from pydantic import BaseModel, Field, ValidationError
from datetime import datetime

class Expense (BaseModel):
    name: str = Field(min_length=4, max_length=30)
    description: str =  None
    amount: float = Field(min=0)
    date: datetime = None
    category_id: int

    class Config:
            orm_mode = True
            schema_extra = {
                "example": {
                    "name": "Gym",
                    "description": "monthly gym",
                    "amount": 10.20,
                    "date": "2024-03-06",
                    "category_id": 1
                }
            }

class ExpenseUpdate (BaseModel):
    name: str = Field(min_length=4, max_length=30)
    description: str =  None
    amount: float = Field(min=0)
    date: datetime = None
    category_id: int
    expense_id: int

    class Config:
            orm_mode = True
            schema_extra = {
                "example": {
                    "name": "Gym",
                    "description": "monthly gym",
                    "amount": 10.20,
                    "date": "2024-03-06",
                    "category_id": 1,
                    "expense_id":1
                }
            }