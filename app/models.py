from flask_restplus import fields

from .api_defination import *
from .main import get_block, write_block, remove_block

block = api.model('Blockchain', {
    'id': fields.Integer(readonly=True, description='Unique identifier'),
    'name': fields.String(required=True, description='Name'),
    'amount': fields.Integer(required=True, description='Amount'),
    'to_whom': fields.String(required=True, description='To whom'),
    'hash': fields.String(readonly=True, required=True, description='Hash'),
})

status = api.model('Status', {
    'block': fields.String(required=True, description='block'),
    'result': fields.String(required=True, description='result'),
})


class BlockchainDAO:
    def __init__(self):
        self.counter = 0
        self.blocks = []

    @staticmethod
    def get(pk):
        try:
            return get_block(pk)
        except (ValueError, TypeError):
            return api.abort(404, "block {} doesn't exist".format(pk))

    def create(self, data):
        _block = data
        _block['id'] = self.counter + 1
        self.blocks.append(_block)
        try:
            write_block(data["name"], data["amount"], data["to_whom"])
        except Exception as e:
            raise e
        return _block

    def update(self, pk, data):
        _block = self.get(pk)
        _block.update(data)
        return _block

    @staticmethod
    def delete(pk):
        remove_block(pk)
