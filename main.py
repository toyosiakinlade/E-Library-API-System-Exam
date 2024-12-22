from fastapi import FastAPI
from pydantic import BaseModel
from routers.books import book_router
from routers.users import user_router
from routers.borrow_record import borrower_router


app = FastAPI()

app.include_router(book_router, prefix='/Books',tags=["Book"])
app.include_router(user_router, prefix='/Users',tags=["Users"])
app.include_router(borrower_router, prefix='/Borrower Operation',tags=["Borrow Operations"])


@app.get("/")
def home():
        return{"Welcome to my E-Library"}


