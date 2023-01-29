from pydantic import BaseModel, validator
from datetime import datetime


class Cart(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: datetime

    @validator('cart_value', 'delivery_distance', 'number_of_items')
    def value_greater_than_zero(cls, value):
        if value <= 0:
            raise ValueError('Value has to be greater than 0')
        return value
