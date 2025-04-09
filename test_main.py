from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}

def test_read_user_me():
    response = client.get("/users/me")
    assert response.status_code == 200