from app.api.models.cart_model import Cart


def calculate_fee(cart: Cart):

    fee = 2  # first 1000 meters
    if cart.cart_value >= 100:
        return 0
    elif cart.cart_value < 10:
        fee += 10-cart.cart_value
    if cart.delivery_distance > 1000:
        fee += round((cart.delivery_distance-1)/1000)
    if cart.number_of_items > 12:
        fee += 1.2
    if cart.number_of_items > 4:
        fee += 0.5*(cart.number_of_items-4)
    if cart.time.weekday() == 4 and 15 <= cart.time.hour and cart.time.hour < 19:
        fee *= 1.2
    if fee > 15:
        return 15
    return fee
