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
from routes.healthcheck.Live import Live
from routes.healthcheck.Ready import Ready
from routes.jira.Proxy import Proxy

# INITIALIZE FLASK
app = Flask(__name__)
api = Api(app)

# API ROUTES
api.add_resource(Index, '/')  # Index Route
api.add_resource(Proxy, '/jira/:query')
app.add_resource(Live, '/healthcheck/live')  # Live Route
app.add_resource(Ready, '/healthcheck/ready')  # Ready Route

# RUN THE APPLICATION
if __name__ == '__main__':
    app.run(port='8080')
