from flask_restful import Resource,request
from app.api.schemas.cart_schema import CartSchema
from marshmallow import ValidationError


class Delivery_calculator(Resource):
    
    def post(self):    
        
        data = request.json            
        
        try:
            validated_data = CartSchema().load(data)            
        except ValidationError as err:
            return err.messages
        
        
        return "validated_data",200