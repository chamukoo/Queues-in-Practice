# producer.py

import pika

QUEUE_NAME = "mailbox"

with pika.BlockingConnection() as connection:
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    while True:
        message = input("Message: ")
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=message.encode("utf-8")
        )



# Apache Kafka: kafka-python3
from kafka3 import kafkaProducer

producer = kafkaProducer(bootsrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    producer.send(
        topic = "datascience",
        value = message.encode("utf-8")
    )