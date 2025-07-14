from flask import Flask
from flask_cors import CORS
from app.extensions import mongo
from app.webhook.routes import webhook
from app.ui.routes import ui

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Configure CORS
    CORS(app)
    
    # Configure MongoDB
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/github_webhooks'
    mongo.init_app(app)
    
    # Register blueprints
    app.register_blueprint(webhook)
    app.register_blueprint(ui)
    
    return app 