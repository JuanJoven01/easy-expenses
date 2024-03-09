from pydantic import BaseModel, Field, ValidationError
from datetime import datetime

# class Dates (BaseModel):
#     initial_date: datetime = None
#     final_date: datetime = None

#     class Config:
#             orm_mode = True
#             schema_extra = {
#                 "example": {
#                     "initial_date": "2024-01-01",
#                     "final_date": "2024-03-08",
#                 }
#             }
