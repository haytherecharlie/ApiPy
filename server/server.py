"""
APIPY - SERVER
-------------------
© 2018 CBC
"""

# IMPORT PACKAGES
from flask import Flask, request
from flask_restful import Resource, Api

# LOCAL IMPORTS
from routes.healthcheck.Live import Live
from routes.healthcheck.Ready import Ready
from routes.index.Default import Default
from routes.jira.Proxy import Proxy

# INITIALIZE FLASK
app = Flask(__name__)
api = Api(app)

# API ROUTES
api.add_resource(Default, '/') # Index Route
api.add_resource(Proxy, '/jira/:query') # Proxy Route
api.add_resource(Live, '/healthcheck/live')  # Live Route
api.add_resource(Ready, '/healthcheck/ready')  # Ready Route

# RUN THE APPLICATION
if __name__ == '__main__':
    app.run(port='8080')
