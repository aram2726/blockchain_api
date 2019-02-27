from flask import Flask

from flask_restplus import Api

app = Flask(__name__)


api = Api(
    app, version='1.0', title='Blockchain API',
    description='Simple API based on Blockchain technology',
)
