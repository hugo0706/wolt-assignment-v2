# import sys
# sys.path.append('.')
import pytest
from pydantic import ValidationError
from app.api.models import delivery_fee_model

@pytest.mark.parametrize(
    "delivery_fee,valid",
    [
        (0,True),
        (1,True),
        (16,False),
        (1000,False),
        (-1,False)
    ]
    )
def test_validate_delivery_fee(delivery_fee,valid):
    
    data={"delivery_fee": delivery_fee}

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