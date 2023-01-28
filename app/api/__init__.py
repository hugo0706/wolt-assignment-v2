from flask_restful import Api
from app import app

from app.api.routes import delivery_calculator
api = Api(app)

api.add_resource(delivery_calculator.Delivery_calculator,"/api")
