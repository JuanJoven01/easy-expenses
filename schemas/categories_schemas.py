from pydantic import BaseModel, Field, ValidationError

class Category (BaseModel):
    name: str

    class Config:
            orm_mode = True
            schema_extra = {
                "example": {
                    "name": "Extra Issues"
                }
            }