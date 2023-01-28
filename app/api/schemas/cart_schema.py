from marshmallow import Schema,fields,validate
import datetime


class CartSchema(Schema):
    cart_value= fields.Integer(required=True,validate=validate.Range(min=0,min_inclusive=False))
    delivery_distance= fields.Integer(required=True,validate=validate.Range(min=0,min_inclusive=False))
    number_of_items= fields.Integer(required=True,validate=validate.Range(min=0,min_inclusive=False))
    time= fields.DateTime(format="iso",required=True)
    
    

   