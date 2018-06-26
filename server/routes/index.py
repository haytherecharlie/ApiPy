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
        return{
            'status': 200,
            'method': 'GET',
            'message': 'Successfully Retrieved Response',
            'payload': {}
        }
