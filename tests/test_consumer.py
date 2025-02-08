from kafka import KafkaConsumer

def test_consumer():
    consumer = KafkaConsumer(
        'test',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        value_deserializer=lambda x: x.decode('utf-8')
    )

    # Verify consumer properties
    assert consumer.bootstrap_servers == ['localhost:9092']
    assert consumer.config['auto_offset_reset'] == 'earliest'
    assert consumer.config['enable_auto_commit'] == False

    # Verify consumer behavior
    consumer.subscribe(['test'])
    assert consumer.subscription() == {'test'}
