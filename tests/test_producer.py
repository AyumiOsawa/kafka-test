from kafka import KafkaProducer

def test_producer():
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"]
    )

    # Verify producer properties
    assert producer.bootstrap_servers == ["localhost:9092"]

    # Verify producer behavior
    future = producer.send("test", value=b"test message")
    result = future.get(timeout=10)
    assert result.topic == "test"
    assert result.value == b"test message"
