"""
 INDEX ROUTE CLASS
-------------------
 © 2018 Charlie Hay
"""

# PACKAGE IMPORTS
from flask_restful import Resource

# INDEX CLASS
class Index(Resource):

    # GET METHOD
    def get(self):
        return {
            'status': 200,
            'method': 'GET',
            'message': 'Successfully Retrieved Response',
            'payload': {}
        }

    # POST METHOD
    def post(self):
        return {
            'status': 200,
            'method': 'POST',
            'message': 'Successfully Retrieved Response',
            'payload': {}
        }

    # PUT METHOD
    def put(self):
        return {
            'status': 200,
            'method': 'PUT',
            'message': 'Successfully Retrieved Response',
            'payload': {}
        }

    def delete(self):
        return {
            'status': 200,
            'method': 'DELETE',
            'message': 'Successfully Retrieved Response',
            'payload': {}
        }

