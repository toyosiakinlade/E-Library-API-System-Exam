from pydantic import BaseModel
from typing import Optional
from datetime import date


class BorrowRecord(BaseModel):
    user_id:int
    book_id:int


class BorrowCreate(BorrowRecord):
    pass

class BorrowReturn(BaseModel):
    return_date: Optional[date] = None