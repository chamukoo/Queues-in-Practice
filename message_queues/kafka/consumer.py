# Apache Kafka: kafka-python3

from kafka3 import kafkaConsumer

consumer = kafkaConsumer("datascience")
for record in consumer:
    message = record.value.decode("utf-8")
    print(f"Got message: {message}")