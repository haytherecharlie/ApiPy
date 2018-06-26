"""
DEFAULT CLASS
-------------------
© 2018 CBC
"""

# IMPORT PACKAGES
from flask_restful import Resource

# PROXY CLASS
class Default(Resource):

	# GET METHOD
	def get(self):
		return{
            'status': 200,
            'method': 'GET',
            'message': 'Welcome to CBC Session API.',
            'payload': {}
        }
