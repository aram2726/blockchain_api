from flask_restplus import Resource
from werkzeug.contrib.fixers import ProxyFix

from .models import app, api, block, status, BlockchainDAO
from .main import check_compatibility


app.wsgi_app = ProxyFix(app.wsgi_app)

namespace = api.namespace('blockchain', description='CRUD operations')


DAO = BlockchainDAO()


@namespace.route('/')
class BlockchainList(Resource):
    """Shows a list of all blocks, and lets you POST to add new blocks"""
    @namespace.doc('list_blocks')
    @namespace.marshal_list_with(status)
    def get(self):
        """List all blocks"""
        return check_compatibility()

    @namespace.doc('create_block')
    @namespace.expect(block)
    @namespace.marshal_with(block, code=201)
    def post(self):
        """Create a new block"""
        return DAO.create(api.payload), 201


@namespace.route('/<int:pk>')
@namespace.response(404, 'block not found')
@namespace.param('pk', 'The task identifier')
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
        """Update block given its identifier"""
        return DAO.update(pk, api.payload)
