# Apache Kafka: kafka-python3
from kafka3 import kafkaProducer

producer = kafkaProducer(bootsrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    producer.send(
        topic = "datascience",
        value = message.encode("utf-8")
    )