from pydantic import BaseModel, validator


class DeliveryFee(BaseModel):
    delivery_fee: int

    @validator('delivery_fee')
    def value_greater_than_zero(cls, value):
        if value <= 0:
            raise ValueError('Value has to be greater than 0')
        return value
