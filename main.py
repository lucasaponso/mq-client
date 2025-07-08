import pika
from constants import rabbit_mq_server_addr

connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_mq_server_addr))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello RabbitMQ!')
print(" [x] Sent 'Hello RabbitMQ!'")
connection.close()
