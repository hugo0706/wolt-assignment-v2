

def test_post_delivery_fee(test_client):
    data = {
        "cart_value": 100,
        "delivery_distance": 1,
        "number_of_items": 1,
        "time": "2021-03-18T16:00:00"
    }
    response = test_client.post('/api/calculate-delivery-fee', json=data)
    assert response.status_code == 200
    assert response.json == {"delivery_fee": 1100}

def test_post_wrong_data(test_client):
    data = {
        "cart_value": 0,
        "delivery_distance": 1,
        "number_of_items": 1,
        "time": "2021-0319T16:00:00"
    }
    response = test_client.post('/api/calculate-delivery-fee', json=data)
    assert response.status_code == 422
    assert "value_error" in response.json[0]["type"]

def test_post_missing_fields(test_client):
    data = {
        "cart_value": 1,
        "delivery_distance": 1,
        "number_of_items": 1
    }
    response = test_client.post('/api/calculate-delivery-fee', json=data)
    assert response.status_code == 422
    assert "value_error.missing" in response.json[0]["type"]

def test_post_bad_request(test_client):
    data = 1
    response = test_client.post('/api/calculate-delivery-fee', data=data)
    assert response.status_code == 400
    assert "Bad Request" in response.json["detail"]