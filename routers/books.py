from fastapi import APIRouter, status
from pydantic import BaseModel
from schemas.books import BookUpdate, BookCreate
from services.books import book_crud


book_router = APIRouter()


@book_router.get("/")
def get_books():
    book = book_crud.get_books()
    return book

@book_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_book(id: int):
    book = book_crud.get_books(id)
    return book

@book_router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(payload:BookCreate):
    new_book = book_crud.create_books(payload)
    return new_book

@book_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_book(id: int, payload:BookCreate):
    book= book_crud.get_book(id)
    update_book = book_crud.update_book(id,data=payload)
    return update_book

@book_router.patch("/{id}", status_code=status.HTTP_200_OK)
def part_update_book(id:int, payload:BookUpdate):
    book = book_crud.get_book(id)
    part_update_book = book_crud.part_update_book(book=book, data=payload)
    return part_update_book

@book_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id:int):
    book_crud.delete_book(id)
    return{"message":"Book deleted successfully!"}