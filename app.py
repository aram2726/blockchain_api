from flask import Flask

from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

import main


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(
    app, version='1.0', title='Blockchain API',
    description='A simple Blockchain API',
)


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


namespace = api.namespace('blockchain', description='CRUD operations')


class BlockchainDAO(object):
    def __init__(self):
        self.counter = 0
        self.blocks = []

    @staticmethod
    def get(pk):
        try:
            return main.get_block(pk)
        except ValueError:
            return api.abort(404, "block {} doesn't exist".format(pk))

    def create(self, data):
        _block = data
        _block['id'] = self.counter = self.counter + 1
        self.blocks.append(_block)
        try:
            main.write_block(**data)
        except Exception as e:
            raise e
        return _block

    def update(self, pk, data):
        _block = self.get(pk)
        _block.update(data)
        return _block

    @staticmethod
    def delete(pk):
        main.remove_block(pk)


DAO = BlockchainDAO()


@namespace.route('/')
class BlockchainList(Resource):
    """Shows a list of all blocks, and lets you POST to add new blocks"""
    @namespace.doc('list_blocks')
    @namespace.marshal_list_with(status)
    def get(self):
        """List all tasks"""
        return main.check_compatibility()

    @namespace.doc('create_block')
    @namespace.expect(block)
    @namespace.marshal_with(block, code=201)
    def post(self):
        """Create a new task"""
        return DAO.create(api.payload), 201


@namespace.route('/<int:id>')
@namespace.response(404, 'block not found')
@namespace.param('id', 'The task identifier')
class Blockchain(Resource):
    """Show a single block item and lets you delete them"""
    @namespace.doc('get_block')
    @namespace.marshal_with(block)
    def get(self, pk):
        """Fetch a given resource"""
        return DAO.get(pk)

    @namespace.doc('delete_block')
    @namespace.response(204, 'block deleted')
    def delete(self, pk):
        """Delete a task given its identifier"""
        DAO.delete(pk)
        return '', 204

    @namespace.expect(block)
    @namespace.marshal_with(block)
    def put(self, pk):
        """Update a task given its identifier"""
        return DAO.update(pk, api.payload)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)
