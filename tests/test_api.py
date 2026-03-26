import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_get_products():
    """Тест получения списка товаров"""
    response = client.get("/products")
    assert response.status_code == 200
