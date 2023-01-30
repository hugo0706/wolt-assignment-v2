from pydantic import BaseModel, validator


class DeliveryFee(BaseModel):
    delivery_fee: int

    @validator('delivery_fee')
    def value_in_range(cls, value):
        if value < 0 or value > 15:
            raise ValueError('Value has to be in range [0 15]')
        return value
    

