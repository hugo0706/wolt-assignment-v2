from flask_restful import Resource, request
from pydantic import ValidationError
from app.api.models import cart_model, delivery_fee_model
from app.api.services.calculate_fee_service import calculate_fee


class Delivery_calculator(Resource):

    def post(self):

        data = request.json

        try:
            validated_data = cart_model.Cart(**data)
        except ValidationError as e:
            return e.errors(), 422

        delivery_fee = calculate_fee(validated_data)
        try:
            delivery_fee_model.DeliveryFee(**delivery_fee)

        except ValidationError as e:
            return e.errors(), 422

        return delivery_fee, 200
