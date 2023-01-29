from flask import Flask
from flask_restful import Api
from app.api.resources import delivery_calculator

def create_app(test_config=None):

    app = Flask(__name__)
    
    api = Api(app)
    
    api.add_resource(delivery_calculator.Delivery_calculator,"/api")   

    return app
    





