import pytest
from src.utils.calculations import calculate_discount

def test_calculate_discount_small_order():
    """Тест расчета скидки для маленького заказа"""
    result = calculate_discount(500, 0)
    assert result == 0  # Нет скидки для заказов меньше 1000

def test_calculate_discount_medium_order():
    """Тест расчета скидки для среднего заказа"""
    result = calculate_discount(2000, 0.05)
    assert result == 100  # 5% от 2000 = 100

def test_calculate_discount_large_order():
    """Тест расчета скидки для большого заказа"""
    result = calculate_discount(6000, 0.1)
    assert result == 600  # 10% от 6000 = 600

def test_calculate_discount_very_large_order():
    """Тест расчета скидки для очень большого заказа"""
    result = calculate_discount(15000, 0.15)
    assert result == 2250  # 15% от 15000 = 2250
