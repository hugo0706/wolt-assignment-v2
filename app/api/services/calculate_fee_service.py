from app.api.models.cart_model import Cart

from math import ceil

def calculate_fee(cart: Cart):
    
    fee = 200  # first 1000 meters
    if cart.cart_value >= 10000:
        return {"delivery_fee": 0}
    elif cart.cart_value < 1000:
        fee += 1000-cart.cart_value
    if cart.delivery_distance > 1000:
        fee += (ceil((cart.delivery_distance)/500)-2)*100
    if cart.number_of_items > 12:
        fee += 120
    if cart.number_of_items > 4:
        fee += 50*(cart.number_of_items-4)
    if cart.time.weekday() == 4 and 15 <= cart.time.hour and cart.time.hour < 19:
        fee *= 1.2
    if fee > 1500:
        return {"delivery_fee": 1500}
    return {"delivery_fee": fee}


