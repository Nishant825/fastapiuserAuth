from pydantic import BaseModel

class UserSchema(BaseModel):
    first_name : str
    last_name : str
    username : str
    email : str
    password : str

    class Config:
        orm_mode = True

    
class LoginSchema(BaseModel):
    username : str
    password : str

    class Config:
        orm_mode = True

    