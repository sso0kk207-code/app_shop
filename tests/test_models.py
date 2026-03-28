from struct import pack

import pytest
from src.models.product import Product
from src.models.user import User
from src.models.order import Order
from src.models.order_validator import OrderValidator
from src.models.payment import CardPayment, PayPalPayment
from src.models.order_calculator import OrderCalculator

@pytest.mark.parametrize("name,price,quantity", [
    ("Ноутбук", 50000, 10),
    ("Ручка", 50, 1000),
    ("Телефон", 30000, 50),
    ("Карандаш", 25, 1)
])
def test_create_product(name, price, quantity):
    """Тест создания товара"""
    product = Product(name, price, quantity)
    assert product.name == name
    assert product.price == price
    assert product.quantity == quantity

@pytest.mark.parametrize("name,price,quantity,expected_value", [
    ("Ноутбук", 50000, 10, 500_000),
    ("Ручка", 50, 1000, 50_000),
    ("Телефон", 30000, 50, 1_500_000),
    ("Карандаш", 25, 1, 25)
])
def test_product_get_total_price(name, price, quantity, expected_value):
    """Тест расчета общей стоимости товара"""
    product = Product(name, price, quantity)
    assert product.get_total_price() == expected_value

@pytest.mark.parametrize("name,email", [
    ("Иван", "ivan@test.com"),
    ("Bob", "bob@go.com"),
    ("Денис", "denis251@mail.ru"),
    ("user52362", "user52362@gmail.com")
])
def test_create_user(name, email):
    """Тест создания пользователя"""
    user = User(name, email)
    assert user.name == name
    assert user.email == email

@pytest.mark.parametrize("username,email,product_name,price,quantity", [
    ("Иван", "ivan@test.com", "Ноутбук", 50000, 10),
    ("Bob", "bob@go.com", "Ручка", 50, 1000),
    ("Денис", "denis251@mail.ru", "Телефон", 30000, 50),
    ("user52362", "user52362@gmail.com", "Карандаш", 25, 1)
])
def test_create_order(username, email, product_name, price, quantity):
    """Тест создания заказа"""
    user = User(username, email)
    product = Product(product_name, price, quantity)
    order = Order(user, [product])
    assert order.user == user
    assert len(order.products) == 1

@pytest.mark.parametrize("username,email,product_name_1,price_1,quantity_1,product_name_2,price_2,quantity_2,total_exp,discount_price_exp,final", [
    ("Иван", "ivan@test.com", "Ноутбук", 50000, 10, "Ручка", 50, 1000, 550_000, 275_000, 275_000),
    ("Bob", "bob@go.com", "Ручка", 50, 1000, "Карандаш", 25, 1, 50_025, 25_012.5, 25_012.5),
    ("Денис", "denis251@mail.ru", "Телефон", 30000, 50, "Карандаш", 25, 1, 1_500_025, 750_012.5, 750_012.5),
    ("user52362", "user52362@gmail.com", "Карандаш", 25, 1, "Ноутбук", 50000, 10, 500_025, 250_012.5, 250_012.5)
])
def test_order_calculate_total(
    username, email, product_name_1, price_1, quantity_1, product_name_2, price_2, quantity_2, total_exp, discount_price_exp, final
    ):
    """Тест калькулятора заказа"""
    calc = OrderCalculator()
    user = User(username, email)
    product1 = Product(product_name_1, price_1, quantity_1)
    product2 = Product(product_name_2, price_2, quantity_2)
    order = Order(user, [product1, product2])
    total = order.calculate_total()
    discount_price = calc.calculate_discount(total=total, discount_rate=0.5)
    assert total == total_exp
    assert discount_price == discount_price_exp
    assert calc.calculate_final_total(total=total, discount=discount_price) == final

@pytest.mark.parametrize("username,email,product_name,price,quantity", [
    ("Иван", "ivan@test.com", "Ноутбук", 50000, 10),
    ("Bob", "bob@go.com", "Ручка", 50, 1000),
    ("Денис", "denis251@mail.ru", "Телефон", 30000, 50),
    ("user52362", "user52362@gmail.com", "Карандаш", 25, 1)
])
def test_validate(username, email, product_name, price, quantity):
    """Тест валидации заказа"""
    validation = OrderValidator()
    user = User(username, email)
    product = Product(product_name, price, quantity)
    order = Order(user, [product])
    assert validation.validate(order)
    assert validation.validate_total(order.calculate_total())

@pytest.mark.parametrize("name,email", [
    ("Иван", "ivan@test.com"),
    ("Bob", "bob@go.com"),
    ("Денис", "denis251@mail.ru"),
    ("user52362", "user52362@gmail.com")
])
def test_users_info(name, email):
    """Тест информации о пользователе"""
    user = User(name, email)
    assert user.get_info() == f"Пользователь: {name}, Email: {email}"

@pytest.mark.parametrize("name,price,quantity,expected_value", [
    ("Ноутбук", 50000, 10, 500_000),
    ("Ручка", 50, 1000, 50_000),
    ("Телефон", 30000, 50, 1_500_000),
    ("Карандаш", 25, 1, 25)
])
def test_total_price(name, price, quantity, expected_value):
    """Тест суммы одного продукта"""
    product = Product(name, price, quantity)
    assert product.get_total_price() == expected_value

@pytest.mark.parametrize("amount,card_number,email", [
    (1000, "1234567812345678", "test@mail.com"),
    (500, "8765432187654321", "paypal@test.com")
])
def test_payments(amount, card_number, email):
    """Тест платежей"""
    card = CardPayment(amount=amount, card_number=card_number)
    paypal = PayPalPayment(amount=amount, email=email)
    assert card.process_payment() == f"Оплата картой **** {card_number[-4:]}: {amount} руб."
    assert paypal.process_payment() == f"Оплата PayPal ({email}): {amount} руб."
