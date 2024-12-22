from fastapi.testclient import TestClient
from main import app  # Replace `main` with the file where your FastAPI app is defined


def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user(client):
    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "is_active": True
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"

def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.status_code == 204
