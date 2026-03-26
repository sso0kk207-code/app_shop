from struct import pack

import pytest
from src.models.product import Product
from src.models.user import User
from src.models.order import Order
from src.models.order_validator import OrderValidator
from src.models.payment import CardPayment, PayPalPayment
from src.models.order_calculator import OrderCalculator

def test_create_product():
    """Тест создания товара"""
    product = Product("Ноутбук", 50000, 10)
    assert product.name == "Ноутбук"
    assert product.price == 50000
    assert product.quantity == 10

def test_product_get_total_price():
    """Тест расчета общей стоимости товара"""
    product = Product("Мышь", 1500, 5)
    assert product.get_total_price() == 7500

def test_create_user():
    """Тест создания пользователя"""
    user = User("Иван", "ivan@test.com")
    assert user.name == "Иван"
    assert user.email == "ivan@test.com"

def test_create_order():
    """Тест создания заказа"""
    user = User("Иван", "ivan@test.com")
    product = Product("Ноутбук", 50000, 1)
    order = Order(user, [product])
    assert order.user == user
    assert len(order.products) == 1

def test_order_calculate_total():
    """Тест калькулятора заказа"""
    calc = OrderCalculator()
    user = User("Иван", "ivan@test.com")
    product1 = Product("Ноутбук", 50000, 1)
    product2 = Product("Мышь", 1500, 2)
    order = Order(user, [product1, product2])
    total = order.calculate_total()
    discount_price = calc.calculate_discount(total=total, discount_rate=0.5)
    assert total == 53000
    assert discount_price == 26500
    assert calc.calculate_final_total(total=total, discount=discount_price) == 26500


def test_validate():
    """Тест валидации заказа"""
    validation = OrderValidator()
    user = User("Иван", "ivan@test.com")
    product = Product("Ноутбук", 50000, 1)
    order = Order(user, [product])
    assert validation.validate(order)
    assert validation.validate_total(order.calculate_total())

def test_users_info():
    """Тест информации о пользователе"""
    user = User("Иван", "ivan@test.com")
    assert user.get_info() == "Пользователь: Иван, Email: ivan@test.com"

def test_total_price():
    """Тест суммы одного продукта"""
    product = Product("Ноутбук", 50000, 2)
    assert product.get_total_price() == 100_000

def test_payments():
    """Тест платежей"""
    card = CardPayment(amount=1000, card_number="1234567812345678")
    paypal = PayPalPayment(amount=500, email="sso0kk207@gmail.com")
    assert card.process_payment() == "Оплата картой **** 5678: 1000 руб."
    assert paypal.process_payment() == "Оплата PayPal (sso0kk207@gmail.com): 500 руб."

