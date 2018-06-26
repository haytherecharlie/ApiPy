"""
LIVE CLASS
-------------------
© 2018 CBC
"""

# PACKAGE IMPORTS
from flask_restful import Resource

# INDEX CLASS
class Live(Resource):

    # GET METHOD
    def get(self):
		return {
            'status': 200,
            'method': 'GET',
            'message': 'App live and responding.',
            'payload': {}
        }