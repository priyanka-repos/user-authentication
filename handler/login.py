import bcrypt
from fastapi import APIRouter
from models.model import UserLogin,User,fgPassword
from database import lib
from fastapi import HTTPException


login_router = APIRouter()

@login_router.post("/login")
def post_user(user:UserLogin):
    
    user_documents =  (lib.find_one({"email":user.email}))
    if user_documents:
        user_documents = dict(user_documents)
        userbytes = user.password.encode('utf-8')    
        result = bcrypt.checkpw(userbytes, user_documents['password'])
        
        if result == True:
            return{"message": "Logged In"}
        else:  
            return{"message":"Incorrect Password"}  
    else:
        raise HTTPException(status_code=404, detail ="User with this email is not Found")

@login_router.post("/forget-password")
def forget_password(user:UserLogin):

    user_documents =  (lib.find_one({"email":user.email}))
    if user_documents:
        # user_documents = dict(user_documents)
        bytes = user.password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        try:
            result=  lib.update_one({"email": user.email}, {"$set": {"password":hash}})
            if result:
                return {"message":"Successfully Password Changed"}
        except Exception as e:
            raise e.args  

    else:
        raise HTTPException(status_code=404, detail ="Incorrect Email Id")
     
       
             
        
    

  
