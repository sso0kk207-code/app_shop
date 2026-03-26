import pika

def process_order_from_queue(ch, method, properties, body):
    """Обработать заказ из очереди RabbitMQ"""
    print(f"Обработан заказ: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
