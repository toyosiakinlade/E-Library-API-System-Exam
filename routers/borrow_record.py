from fastapi import APIRouter, HTTPException, status
from schemas.borrow_record import BorrowCreate, BorrowReturn
from services.borrow_record import borrow_crud


borrower_router = APIRouter()


@borrower_router.post("/ borrow", status_code=status.HTTP_201_CREATED)
def borrow_book(payload:BorrowCreate):
    borrowed_book= borrow_crud.borrow_book(user_id=payload.user_id, book_id=payload.book_id)
    return{"message": "Book borrowed successfully", "data":borrowed_book}


@borrower_router.get("/", status_code=status.HTTP_200_OK)
def get_borrow_records():
    records = borrow_crud.get_borrow_records()
    if not records:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No borrow record found.")
    return records

@borrower_router.get("/{id}")
def get_borrow_record(id: int):
    record = borrow_crud.get_borrow_record(id)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=" Borrowed record not found.")
    return record


@borrower_router.post("/return", status_code=status.HTTP_201_CREATED)
def return_book(payload:BorrowReturn):
    returned_book= borrow_crud.return_book(user_id=payload.user_id, book_id=payload.book_id)
    return{"message": "Book returned successfully", "data":returned_book}
