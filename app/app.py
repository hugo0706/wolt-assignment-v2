from flask import Flask,Blueprint
from flask_restful import Api
from app.api.resources import delivery_fee_resource


def create_app():
    
    
    app = Flask(__name__)
    api_bp = Blueprint("api", __name__, url_prefix="/api")

    api = Api(api_bp)
    api.add_resource(delivery_fee_resource.Delivery_calculator, "/calculate-delivery-fee")

    app.register_blueprint(api_bp)

    return app


