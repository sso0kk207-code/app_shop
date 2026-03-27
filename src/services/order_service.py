from src.models.order import Order
from src.services.queue_producer import send_order_to_queue

def process_order_async(order: Order):
    """Обработать заказ асинхронно через очередь"""
    # Отправка заказа в очередь для обработки
    order_data = {
        "order_id": order.id,
        "user_id": order.user.id if order.user else None,
        "total": order.calculate_total(),
        "items": [{"product_id": item.id, "quantity": item.quantity} for item in order.products]
    }
    
    send_order_to_queue(order_data)
    print(f"Заказ {order.id} отправлен в очередь для обработки")
