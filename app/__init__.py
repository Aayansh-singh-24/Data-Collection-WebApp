import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    """
    Application factory that configures Flask for different environments
    (development vs production) based on environment variables.
    """
    
    # Load environment variables from .env (for local/dev)
    load_dotenv()

    from .config import DevelopmentConfig, ProductionConfig

    app = Flask(__name__)

    flask_env = os.environ.get("FLASK_ENV", "development").lower()
    if flask_env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    
    with app.app_context():
        from . import models  
        from .routes import register_blueprints
        from .auth import register_auth_blueprint

        register_blueprints(app)
        register_auth_blueprint(app)
        db.create_all()

    return app


@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))

