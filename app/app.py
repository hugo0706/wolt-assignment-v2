from flask import Flask
from flask_restful import Api
from app.api.resources import delivery_fee_resource


def create_app(config=None):
    
    
    app = Flask(__name__)
    
    api = Api(app)

    api.add_resource(delivery_fee_resource.Delivery_calculator, "/api/calculate-delivery-fee")

    return app


