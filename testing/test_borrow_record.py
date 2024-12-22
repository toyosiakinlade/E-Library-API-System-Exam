from fastapi.testclient import TestClient
from main import app  # Replace `main` with the file where your FastAPI app is defined


def test_borrow_book(client):
    payload = {
        "user_id": 1,
        "book_id": 1
    }
    response = client.post("/borrow-record/borrow", json=payload)
    assert response.status_code == 201
    assert response.json()["message"] == "Book borrowed successfully"

def test_return_book(client):
    payload = {
        "user_id": 1,
        "book_id": 1,
        "return_date": "2024-12-25"
    }
    response = client.post("/borrow-record/return", json=payload)
    assert response.status_code == 201
    assert response.json()["message"] == "Book returned successfully"
