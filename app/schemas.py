from datetime import date
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    nombre: str
    apellido: str
    fecha: Optional[date] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
