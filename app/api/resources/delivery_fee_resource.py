from flask_restful import Resource, request
from pydantic import ValidationError
from app.api.models import cart_model, delivery_fee_model
from app.api.services.calculate_fee_service import calculate_fee
from app.api import error_handlers



class Delivery_calculator(Resource):

    def post(self):
        try:

            data = dict(request.get_json())

        except Exception as e:
            raise error_handlers.WrongJSON()

        try:
            validated_data = cart_model.Cart(**data)

            delivery_fee = calculate_fee(validated_data)

            delivery_fee_model.DeliveryFee(**delivery_fee)

        except ValidationError as e:
            return e.errors(), 422

        return delivery_fee, 200
