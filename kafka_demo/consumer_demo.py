from kafka import KafkaConsumer


def main():
    consumer = KafkaConsumer('start_in_cont')
    print("Topics: ", consumer.topics())
    # print("Next: ", consumer.next())
    for msg in consumer:
        print("Message: ", msg)


if __name__ == '__main__':
    main()
