from typing import Union
from pydantic import BaseModel
from typing import List
from .models import User, Gender, Roles
from fastapi import FastAPI, APIRouter
from uuid import uuid4




db: List[User] = [
    User(
        id=uuid4(),
        first_name="Ornelio",
        last_name="Chau",
        midlle_name="da Almina",
        gender=Gender.male,
        role=[Roles.student],
    ),
    User(
        id=uuid4(),
        first_name="Paulo",
        last_name="Chau",
        midlle_name="Agostinho",
        gender=Gender.female,
        role=[Roles.admin, Roles.user],
    ),
]   