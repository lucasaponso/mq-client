import pika
from constants import rabbit_mq_server_addr
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_mq_server_addr))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.star
