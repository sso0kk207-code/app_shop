import pika

def send_order_to_queue(order_data):
    """Отправить заказ в очередь RabbitMQ"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='orders')
    channel.basic_publish(exchange='', routing_key='orders', body=str(order_data))
    connection.close()
