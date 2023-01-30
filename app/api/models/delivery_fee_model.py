from pydantic import BaseModel, validator


class DeliveryFee(BaseModel):
    delivery_fee: int

    @validator('delivery_fee')
    def value_in_range(cls, value):
        if value < 0 or value > 1500:
            raise ValueError('Value has to be in range [0 1500]')
        return value
    

