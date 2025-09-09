from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, APIRouter
from db import db


router = APIRouter()

app = FastAPI()

    

class User(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    is_Seller: bool

@app.get("/create/user", status_code=200)
async def create_user():
    return {"hello": "mundao"}
    

app.include_router(router)