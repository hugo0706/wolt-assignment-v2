from flask import Flask


#def create_app(test_config=None):

app = Flask(__name__)

from .api import api    

apiResource = api

#    return app