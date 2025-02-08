from app.enqueue_json import enqueue_json
from unittest.mock import MagicMock

def test_enqueue_json():
    # Create a mock Kafka producer
    mock_producer = MagicMock()
    
    # Replace the producer in the enqueue_json module with the mock producer
    enqueue_json.producer = mock_producer
    
    # Call enqueue_json with sample JSON data
    sample_json_data = '{"key": "value"}'
    enqueue_json(sample_json_data)
    
    # Verify the producer's behavior
    mock_producer.send.assert_called_once_with("test", value=sample_json_data.encode("utf-8"))
