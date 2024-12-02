from kafka import KafkaProducer


producer = KafkaProducer(
      bootstrap_servers=["localhost:9092"]
  )

TOPIC = "test"

def main():
  while True:
    # Get userinput from the CLI:
    input_str = input("Enter a message (type 'quit' to finish): ")
    if input_str.strip() == "quit":
      print('Quiting the producer')
      break
    producer.send(TOPIC, value=input_str.encode("utf-8"))


if __name__ == "__main__":
  main()


