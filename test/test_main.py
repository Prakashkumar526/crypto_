from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_coins():
    response = client.get("/coins", auth=("admin", "admin"))
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_categories():
    response = client.get("/categories", auth=("admin", "admin"))
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_coin():
    response = client.get("/coins/bitcoin", auth=("admin", "admin"))
    assert response.status_code == 200
    assert response.json()["id"] == "bitcoin"
