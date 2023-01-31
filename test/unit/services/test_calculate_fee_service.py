import pytest
from app.api.models import cart_model
from app.api.services import calculate_fee_service
from test.read_test_data import read_test_data

data=read_test_data()

@pytest.mark.parametrize("cart_info,value",
    data["fee_service"]
)
def test_calculate_fee(cart_info,value):
    
    data= cart_model.Cart(**cart_info)
    
    fee = calculate_fee_service.calculate_fee(data)
    assert fee == value
    