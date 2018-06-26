"""
PROXY CLASS
-------------------
© 2018 CBC
"""

# PACKAGE IMPORTS
from flask_restful import Resource

# PROXY CLASS
class Proxy(Resource):

	# GET METHOD
	def get(self):
		return{
            'status': 200,
            'method': 'GET',
            'message': 'Jira proxy success',
            'payload': {}
        }