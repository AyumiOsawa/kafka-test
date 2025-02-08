import os
import json

def test_storage():
    path = os.path.join('app', 'storage', 'test_data.json')
    with open(path, 'r') as file:
        json_data = json.load(file)
    
    assert isinstance(json_data, dict)
    assert 'test' in json_data
    assert 'timestamp' in json_data

    test_data = json_data['test']
    assert 'msg' in test_data
    assert 'data' in test_data

    msg_data = test_data['msg']
    assert isinstance(msg_data, list)
    assert len(msg_data) == 2
    assert msg_data[0] == "this is some test message from a JSON file."
    assert msg_data[1] == "long massage"

    data = test_data['data']
    assert 'name' in data
    assert 'age' in data
    assert 'city' in data
    assert data['name'] == "John Doe"
    assert data['age'] == 30
    assert data['city'] == "New York"

    assert json_data['timestamp'] == 1600000000
