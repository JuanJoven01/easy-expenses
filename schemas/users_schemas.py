from pydantic import BaseModel, Field, ValidationError

class User (BaseModel):
    username: str = Field(max_length=15, min_length=4)
    password: str = Field(min_length=8)

    class Config:
            orm_mode = True
            schema_extra = {
                "example": {
                    "name": "ImPablo",
                    "password": "verysecurepassword"
                }
            }

class UserNewPass (BaseModel):
    password: str = Field(min_length=8)
    new_password: str = Field(min_length=8)

    class Config:
            orm_mode = True
            schema_extra = {
                "example": {
                    "name": "ImPablo",
                    "password": "verysecurepassword",
                    "new_password": "verysecurepassword2"
                }
            }