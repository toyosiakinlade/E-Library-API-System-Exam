from typing import Optional
from pydantic import BaseModel



class BookBase(BaseModel):
    title:str
    author:str
    is_available:bool

class Book(BookBase):
    id:int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title:Optional[str] = None
    author:Optional[str] = None
    is_available:Optional[str] = None