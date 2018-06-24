"""
 APIPY - SERVER
-------------------
 © 2018 Charlie Hay
"""

# IMPORT PACKAGES
from flask import Flask, request
from flask_restful import Resource, Api

# LOCAL IMPORTS
from routes.index import Index

# INITIALIZE FLASK
app = Flask(__name__)
api = Api(app)

# API ROUTES
api.add_resource(Index, '/') # Index Route

# RUN THE APPLICATION
if __name__ == '__main__':
    app.run(port='8080')
