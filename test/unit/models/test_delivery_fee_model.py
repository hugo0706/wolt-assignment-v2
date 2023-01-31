import pytest
from pydantic import ValidationError
from app.api.models import delivery_fee_model
from test.read_test_data import read_test_data

data = read_test_data()
@pytest.mark.parametrize(
    "data,valid",
    data['delivery_fee_validate']
    )
def test_validate_delivery_fee(data,valid):

    try:
        delivery_fee = delivery_fee_model.DeliveryFee(**data)
        assert valid
        assert delivery_fee.delivery_fee == delivery_fee.delivery_fee
    except ValidationError:
        assert not valid

def test_missing_value():
    data = {}
    with pytest.raises(ValidationError):
        delivery_fee_model.DeliveryFee(**data)