
import sys
sys.path.append('.')
import pytest
from pydantic import ValidationError
from app.api.models import cart_model



@pytest.mark.parametrize(
    "cart_value,delivery_distance,number_of_items,time,valid",
    [
        (1,1,1,"2021-03-19T16:00:00",True),
        (1000,1000,1000,"2023-01-20T10:00:00",True),
        (0,1,1,"2021-03-19T16:00:00",False),
        (1,0,1,"2021-03-19T16:00:00",False),
        (1,1,0,"2021-03-19T16:00:00",False),
        (1,1,1,"2021-0319T16:00:00",False)
    ]
)

def test_validate_cart(cart_value,delivery_distance,number_of_items,time,valid):

    data = {
        "cart_value": cart_value,
        "delivery_distance": delivery_distance,
        "number_of_items": number_of_items,
        "time": time
    }
    try:
        cart = cart_model.Cart(**data)
        assert valid

        assert cart.cart_value == cart_value
        assert cart.delivery_distance == delivery_distance
        assert cart.number_of_items == number_of_items
        assert cart.time.isoformat() == time
    except ValidationError:
        assert not valid



def test_missing_fields():
    data = {
        "cart_value": 1,
        "delivery_distance": 1,
        "number_of_items": 1
    }
    with pytest.raises(ValidationError):
        cart = cart_model.Cart(**data)
    data = {
        "cart_value": 1,
        "delivery_distance": 1,
        "time": "2021-0319T16:00:00"
    }
    with pytest.raises(ValidationError):
        cart = cart_model.Cart(**data)
    data = {
        "cart_value": 1,
        "number_of_items": 1,
        "time": "2021-0319T16:00:00"
    }
    with pytest.raises(ValidationError):
        cart = cart_model.Cart(**data)
    data = {
        "delivery_distance": 1,
        "number_of_items": 1,
        "time": "2021-0319T16:00:00"
    }
    with pytest.raises(ValidationError):
        cart = cart_model.Cart(**data)

    
if __name__ == "__main__":
    pytest.main()