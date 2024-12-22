from typing import Optional
from pydantic import BaseModel



class UserBase(BaseModel):
    name:str
    email:str
    is_active:bool

class User(UserBase):
    id:int

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name:Optional[str] = None
    email:Optional[str] = None
    is_active:Optional[str] = None