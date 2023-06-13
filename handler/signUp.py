import bcrypt
from fastapi import APIRouter
from models.model import User
from database import lib
signup_router = APIRouter()

@signup_router.get("/signup")
def get_user():
    return {"message" : "Ok"}

@signup_router.post("/signup")
def post_user(user: User):
    
    password = b'{user.password}'
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    
    insert_user = {
        "name": user.name,
        "email": user.email,
        "password": hashed
    }
    lib.insert_one(dict(insert_user))
    return {"user":dict(insert_user)}
    
