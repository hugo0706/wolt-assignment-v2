from flask_restful import Resource,request
from pydantic import ValidationError
from app.api.models.cart import Cart

class Delivery_calculator(Resource):
    
    def post(self):    
        
        data = request.json            
        
        try:
            a=Cart(**data)
        except ValidationError as e:
            return e.errors(),422 
                
        return "validated_data",200