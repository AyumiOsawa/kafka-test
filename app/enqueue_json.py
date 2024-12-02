import os

from app.producer import producer

TOPIC = "test"

def enqueue_json(json_data):
  producer.send(TOPIC, value=json_data.encode("utf-8"))

def main():
  # Get file name from the user.
  while True: 
    filename = input("Enter a filename to enqueue JSON data (enter 'quit' to exit): ")
    if filename.strip() == "quit":
      print("Quiting the file enqueuing process")
      return
    path = os.path.join('app', 'storage', filename)
    if not os.path.exists(path):
      print("File does not exist in the storage directory. Please enter a valid filename. Checked path: ", path)
      continue
    with open(path, "r") as file:
      json_data = file.read()
      enqueue_json(json_data)
      print(f"Enqueued JSON data from file {filename} successfully.")


if __name__ == "__main__":
  main()