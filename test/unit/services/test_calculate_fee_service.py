import pytest
from app.api.models import cart_model
from app.api.services import calculate_fee_service
from pydantic import ValidationError

@pytest.mark.parametrize(
    "cart_info,value",
    [
        (
            {"cart_value": 100, "delivery_distance": 1, "number_of_items": 1, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1100}
        ),
        (
            {"cart_value": 100, "delivery_distance": 1, "number_of_items": 1, "time": "2023-01-27T18:10:00Z"},
            {"delivery_fee":1320}
        ),
        (
            {"cart_value": 100, "delivery_distance": 1000, "number_of_items": 1, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1100}
        ),
        (
            {"cart_value": 100, "delivery_distance": 1001, "number_of_items": 1, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1200}
        ),
        (
            {"cart_value": 100, "delivery_distance": 1500, "number_of_items": 1, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1200}
        ),
        (
            {"cart_value": 100, "delivery_distance": 1501, "number_of_items": 1, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1300}
        ),
        (
            {"cart_value": 100, "delivery_distance": 1, "number_of_items": 4, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1100}
        ),
        (
            {"cart_value": 100, "delivery_distance": 1, "number_of_items": 6, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1200}
        ),
        (
            {"cart_value": 100, "delivery_distance": 1, "number_of_items": 12, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1500}
        ),
        (
            {"cart_value": 100, "delivery_distance": 1, "number_of_items": 13, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1500}
        ),
        (
            {"cart_value": 1000, "delivery_distance": 1, "number_of_items": 13, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":770}
        ),
        (
            {"cart_value": 100, "delivery_distance": 50000, "number_of_items": 23, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":1500}
        ),
        (
            {"cart_value": 10000, "delivery_distance": 50000, "number_of_items": 23, "time": "2023-01-26T18:10:00Z"},
            {"delivery_fee":0}
        ),
        
    ]
)
def test_calculate_fee(cart_info,value):
    print(cart_info)
    data= cart_model.Cart(**cart_info)

    try:
        fee = calculate_fee_service.calculate_fee(data)
        assert fee == value
    except ValidationError:
        assert not True