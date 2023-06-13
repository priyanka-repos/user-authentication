import bcrypt
from fastapi import APIRouter
from models.model import UserLogin,User
from database import lib
from fastapi import HTTPException


login_router = APIRouter()



@login_router.post("/login")
def post_user(user:UserLogin):

    password = b'{user.password}'
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)

    user_documents =  dict(lib.find_one({"email":user.email},{'_id':False}))
    print(user_documents["password"])
    # for user in user_documents:
    #     print()
    # if hashed == user_documents.password:
    #     return {"data":user_documents}
    
    # raise HTTPException(status_code=401, detail="Invalid credentials.")
    # print(user_documents)
   
    