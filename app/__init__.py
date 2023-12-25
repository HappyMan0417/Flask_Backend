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
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://test:future417@localhost/test"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # import Blueprints here to avoid circular imports
    from .views.user_views import example_blueprint
    app.register_blueprint(example_blueprint)

    return app