# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv
# import os

# from app.views.user_views import example_blueprint


# load_dotenv()

# app = Flask(__name__)

# # MySQL configurations
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://test:future417@localhost/test"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# app.register_blueprint(example_blueprint)

# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    server = Flask(__name__)
    server.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://test:future417@db/test"
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(server)

    # import Blueprints here to avoid circular imports
    from .views.user_views import example_blueprint
    server.register_blueprint(example_blueprint)

    return server