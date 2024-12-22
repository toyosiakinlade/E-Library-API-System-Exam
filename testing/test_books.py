from fastapi.testclient import TestClient
from main import app 


def test_get_books(client):
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_book(client):
    payload = {
        "title": "New Book",
        "author": "Author Name",
        "is_available": True
    }
    response = client.post("/books/", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "New Book"

def test_delete_book(client):
    response = client.delete("/books/1")
    assert response.status_code == 204
