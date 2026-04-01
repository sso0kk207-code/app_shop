import pytest
from fastapi.testclient import TestClient
from src.api.main import app
from src.api.auth import verify_token

client = TestClient(app)

def test_get_product():
    """Тест получения данных о продукте"""
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json()) == 3

def read_root():
    """Тест получения приветственного сообщения"""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Добро пожаловать в SFMShop API"}

@pytest.mark.parametrize("product_id, expected", [
    (1, {"id": 1, "name": "Ноутбук", "price": 50000, "quantity": 10}),
    (2, {"id": 2, "name": "Мышь", "price": 1500, "quantity": 20}),
    (3, {"id": 3, "name": "Клавиатура", "price": 3000, "quantity": 15}),
    (999, {"error": "Товар не найден"})
])
def test_get_product_by_id(product_id, expected):
    """Тест получения данных о продукте по ID"""
    response = client.get(f"/products/{product_id}")

    assert response.status_code == 200
    assert response.json() == expected

@pytest.fixture
def order_data():
    """Фикстура для данных заказа"""
    return {
        "user_id": 1,
        "product_id": 1,
        "quantity": 2
    }

def test_create_order(order_data):
    """Тест создания заказа"""
    response = client.post("/orders", json=order_data)
    assert response.status_code == 200
    assert response.json() == {
        "id": 5,
        "user_id": order_data["user_id"],
        "product_id": order_data["product_id"],
        "quantity": order_data["quantity"],
        "message": "Заказ создан"
    }

def test_verify_token():
    """Тест проверки токена"""
    token = "valid_token"
    result = verify_token(token)
    assert result == token