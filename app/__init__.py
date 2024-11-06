from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Import and register routes
    from .routes import contact_blueprint, health_blueprint
    app.register_blueprint(contact_blueprint, url_prefix='/api')
    app.register_blueprint(health_blueprint, url_prefix='/api')

    return app
