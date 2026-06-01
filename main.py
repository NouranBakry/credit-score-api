from fastapi import FastAPI
from database import engine, Base
from models import User
from routers import validate_user

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


# app.include_router(validate_user.router)
