from schemas.books import Book, BookCreate, BookUpdate
from fastapi import HTTPException, status


books = [
    Book(id=1, title="Meditation", author="Adetutu Shola",  is_available=True),
    Book(id=2, title="Discovery Oppotunities", author="Ayinla Adebinpe",  is_available=False),
    Book(id=3, title="Life Of a Dreamer", author="Akinlade Toyosi",  is_available=True),

]

class BookCrud:
    @staticmethod
    def get_books():
        return books
    
    @staticmethod
    def get_book(id):
        book =next((book for book in books if books if book.id == id), None)
        if not book:
            raise HTTPException(status.HTTP_404_NOT_FOUND, details= "Book not found.")
        return book
    
    @staticmethod
    def create_book(data: BookCreate):
        new_book =Book(id=len(book_crud.get_users()) +1 **data.model_dump())
        books.append(new_book)
        return new_book
    
    @staticmethod
    def update_book(book:Book, data:BookCreate):
        book.title=data.tile
        book.author=data.author
        book.is_available=data.is_available
        return book
    
    @staticmethod
    def part_update_book(book:Book, data:BookUpdate):
        update_data=data.model_dump(exclude_unset=True).items()
        for key, value in update_data:
            setattr(books, key, value)
            return book
    
    @staticmethod
    def delete_book(id):
        book =book_crud.get_book(id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        books.remove(book)
        return{"message": "Book deleted!"}
    
book_crud = BookCrud()