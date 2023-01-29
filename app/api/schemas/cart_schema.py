from marshmallow import Schema,fields,validate,post_load
from app.api.models.cart import Cart


class CartSchema(Schema):
    cart_value= fields.Integer(required=True,validate=validate.Range(min=0,min_inclusive=False))
    delivery_distance= fields.Integer(required=True,validate=validate.Range(min=0,min_inclusive=False))
    number_of_items= fields.Integer(required=True,validate=validate.Range(min=0,min_inclusive=False))
    time= fields.DateTime(format="iso",required=True)
    
    @post_load
    def create_cart(self,data,**kwargs):
        return Cart(**data)
    

   