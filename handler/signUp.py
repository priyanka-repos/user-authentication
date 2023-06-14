import bcrypt
from fastapi import APIRouter
from models.model import User
from database import lib
from fastapi import HTTPException, status
signup_router = APIRouter()

@signup_router.get("/signup")
def get_user():
    return {"message" : "Ok"}

@signup_router.post("/signup")
def post_user(user: User):
    user_documents =  lib.find_one({"$or":[{"email":user.email},{"name":user.name}]})

    if user_documents:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    else:
        bytes = user.password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        
        insert_user = {
            "name": user.name,
            "email": user.email,
            "password": hash
        }
        lib.insert_one(dict(insert_user))
        return {"user":dict(insert_user)}
    

