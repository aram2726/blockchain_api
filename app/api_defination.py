from flask import Flask

from flask_restplus import Api

app = Flask(__name__)


api = Api(
    app,
    version='1.0',
    title='Blockchain API',
    description='Simple API based on Blockchain technology',
    contact='email aramharoyan@gmail.com',
    contact_email='aramharoyan@gmail.com',
    license='License MIT',
    license_url='https://github.com/aram2726/blockchain_api/blob/master/LICENSE',
)
