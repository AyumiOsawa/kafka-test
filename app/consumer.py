from kafka import KafkaConsumer

TOPIC = "test"
consumer = KafkaConsumer(TOPIC,
                        bootstrap_servers=['localhost:9092'],
                        auto_offset_reset='earliest',
                        enable_auto_commit=False,
                        # group_id='my_group_id',
                        value_deserializer=lambda x: x.decode('utf-8')
                        )

def main():
  for message in consumer:
    print("Received message: ", message.value)
    print(dir(message))
    input_str = input("Press enter to receive more message (type 'quit' to finish): ")
    if input_str.strip() == "quit":
      print('Quiting the consumer')
      break


if __name__ == "__main__":
  main()