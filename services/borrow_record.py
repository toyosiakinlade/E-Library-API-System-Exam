from fastapi import HTTPException, status
from datetime import date
from schemas.borrow_record import BorrowCreate, BorrowReturn

borrow_records_data = []

class BorrowService:
    @staticmethod
    def borrow_book(user_id: int, book_id: int):
        # Check if the user has already borrowed this book
        existing_record = next(
            (record for record in borrow_records_data if record["user_id"] == user_id and record["book_id"] == book_id),
            None
        )
        if existing_record:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already borrowed this book.")
        
        # Create a new borrow record
        new_record = {
            "id": len(borrow_records_data) + 1,
            "user_id": user_id,
            "book_id": book_id,
            "borrowed_date": date.today(),
            "return_date": None,
        }
        borrow_records_data.append(new_record)
        return new_record

    @staticmethod
    def return_book(user_id: int, book_id: int, return_date: date):
        record = next(
            (record for record in borrow_records_data if record["user_id"] == user_id and record["book_id"] == book_id),
            None
        )
        if not record or record["return_date"]:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Borrow record not found.")
        
        if return_date < record["borrowed_date"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Return date cannot be before borrow date.")

        record["return_date"] = return_date
        return record

    @staticmethod
    def get_borrow_records():
        return borrow_records_data

    @staticmethod
    def get_borrow_record(id: int):
        record = next((record for record in borrow_records_data if record["id"] == id), None)
        if not record:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Borrow record not found.")
        return record

borrow_crud = BorrowService()
