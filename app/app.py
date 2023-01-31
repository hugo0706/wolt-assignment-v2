from flask import Flask,Blueprint
from flask_restful import Api
from app.api.resources import delivery_fee_resource

from flasgger import Swagger
from flasgger.utils import swag_from
from app.api.config.swagger import template, swagger_config

def create_app():
    
    
    app = Flask(__name__)
    api_bp = Blueprint("api", __name__, url_prefix="/api")

    api = Api(api_bp)
    api.add_resource(delivery_fee_resource.Delivery_calculator, "/calculate-delivery-fee")
    
    app.register_blueprint(api_bp)

    app.config["SWAGGER"] = {
        "title": "Cart delivery fee calculator",
        "uiversion": 3
    }
    Swagger(app, template=template, config=swagger_config)

    return app
