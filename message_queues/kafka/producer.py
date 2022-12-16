# Apache Kafka: kafka-python3

from kafka import KafkaProducer

producer = KafkaProducer(bootsrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    producer.send(
        topic = "datascience",
        value = message.encode("utf-8")
    )