# /app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
# from .db import db

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://ask:Schnebber69@db:5432/RESTtestdb')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from .resources import DataResource
    api = Api(app)
    api.add_resource(DataResource, '/data')

    with app.app_context():
        db.create_all()

    return app
