import pytest
from src.utils.calculations import calculate_discount, calculate_delivery, calculate_final_price

@pytest.mark.parametrize("price,discount_rate,expected_value", [
    (500, 0, 0),
    (2000, 0.05, 100),
    (6000, 0.1, 600),
    (15000, 0.15, 2250)
])
def test_calculate_discount_small_order(price, discount_rate, expected_value):
    """Тест расчета скидки для заказа"""
    assert calculate_discount(price, discount_rate) == expected_value

@pytest.mark.parametrize("weight,base_cost,expected_value", [
    (1, 100, 110),
    (0.5, 300, 305),
    (100, 1000, 2000)
])
def test_calculate_delivery(weight, base_cost, expected_value):
    """Тест расчета доставки"""
    assert calculate_delivery(weight, base_cost) == expected_value

@pytest.mark.parametrize("price,discount,delivery,expected_value", [
    (400, 100, 100, 400),
    (100, 0, 10, 110),
    (1000, 900, 100, 200)
])
def test_calculate_final_price(price, discount, delivery, expected_value):
    """Тест расчета финальной суммы"""
    assert calculate_final_price(price, discount, delivery) == expected_value
