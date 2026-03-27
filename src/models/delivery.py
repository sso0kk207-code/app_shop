from abc import ABC, abstractmethod

class Delivery(ABC):
    """Абстрактный класс для доставки"""
    
    @abstractmethod
    def calculate_cost(self, distance: float) -> float:
        """Рассчитать стоимость доставки"""
        pass

class StandardDelivery(Delivery):
    """Стандартная доставка"""
    
    def calculate_cost(self, distance: float) -> float:
        return distance * 10

class ExpressDelivery(Delivery):
    """Экспресс-доставка"""
    
    def calculate_cost(self, distance: float) -> float:
        return distance * 20
