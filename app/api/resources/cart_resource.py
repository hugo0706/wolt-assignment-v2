from flask_restful import Resource,request
from pydantic import ValidationError
from app.api.models.cart_model import Cart
from app.api.services.calculate_fee_service import calculate_fee

class Delivery_calculator(Resource):
    
    def post(self):    
        
        data = request.json            
        
        try:
            validated_data = Cart(**data)
        except ValidationError as e:
            return e.errors(),422 

        print(validated_data.time.weekday()) 
        a= calculate_fee(validated_data)
        print(a)

        return "validated_data",200