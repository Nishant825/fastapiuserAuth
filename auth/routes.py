from fastapi import FastAPI, Depends
from .schemas import UserSchema, LoginSchema
from .models import User, Token
from .db import get_db
from .utils import get_password_hash, verify_password, create_access_token, has_access
from sqlalchemy.orm import Session


app = FastAPI()

@app.post("/create_user")
async def create_user(user: UserSchema,db: Session=Depends(get_db)):
    user = User(username=user.username,email=user.email,password=get_password_hash(user.password),first_name=user.first_name,last_name=user.last_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    response = {"message":"user registered successfully"}
    return response


@app.post("/user_login")
async def login_user(user: LoginSchema,db: Session=Depends(get_db)):
    user_obj = db.query(User).filter(User.username == user.username).first()
    if user_obj is None:
        return {"message":"user not exist"}
    password = verify_password(user.password, user_obj.password)
    if user_obj and password:
        token_obj = db.query(Token).filter(Token.user_id==user_obj.id).first()
        if token_obj:
            response = {"access_token":token_obj.access_token}
        else:
            token_key = create_access_token(user_obj.username)
            token = Token(access_token=token_key,user_id=user_obj.id)
            db.add(token)
            db.commit()
            db.refresh(token)
            response = {"access_token":token_key}
        return response
    return {"message":"error occured"}



@app.get("/get_user")
async def create_user(current_user: User = Depends(has_access)):
    response = {
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "username": current_user.username,
        "email": current_user.email
                }
    return response

