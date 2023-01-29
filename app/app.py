from flask import Flask
from flask_restful import Api
from app.api.resources import cart_resource

def create_app(test_config=None):

    app = Flask(__name__)
    
    api = Api(app)
    
    api.add_resource(cart_resource.Delivery_calculator,"/api/get-delivery-fee")   

    return app
    





