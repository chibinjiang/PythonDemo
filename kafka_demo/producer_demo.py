from kafka import KafkaProducer


def publish_message(producer_instance: KafkaProducer, topic_name: str, key: str, value: str):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        print('1')
        status = producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        status.succeeded()
        status.failed()
        print('2')
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def main():
    topic = "kafka_demo"
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    for i in range(100):
        publish_message(producer, topic, f"Key: {i}", f"Hello, Zhibin Jiang : {i}")


if __name__ == '__main__':
    main()
