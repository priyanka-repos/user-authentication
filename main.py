from fastapi import FastAPI
from handler.signUp import signup_router
from handler.login import login_router
app = FastAPI()

app.include_router(signup_router, prefix='/users')
app.include_router(login_router)

