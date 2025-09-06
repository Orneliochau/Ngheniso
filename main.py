from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI, APIRouter

router = APIRouter()

app = FastAPI()

class User(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    is_Seller: bool

@router.post("/create/user", status_code=201)
async def create_user(User: User):
    return {"status": "Sucessfull"}
    

app.include_router(router)