
# import sys
# sys.path.append('.')
import pytest
from pydantic import ValidationError
from app.api.models import cart_model
from app.test.read_test_data import read_test_data

data = read_test_data()

@pytest.mark.parametrize(
    "data,valid",
    data["cart_model_validate"])
def test_validate_cart(data, valid):

    try:
        cart = cart_model.Cart(**data)
        assert valid["valid"]

        assert cart.cart_value == data["cart_value"]
        assert cart.delivery_distance == data["delivery_distance"]
        assert cart.number_of_items == data["number_of_items"]
        assert cart.time.isoformat() == data["time"]
    except ValidationError:
        assert not valid["valid"]


@pytest.mark.parametrize("data_missing_field",
    data["cart_model_missing_fields"]
)
def test_missing_fields(data_missing_field):
    
    with pytest.raises(ValidationError):
        cart = cart_model.Cart(**data)