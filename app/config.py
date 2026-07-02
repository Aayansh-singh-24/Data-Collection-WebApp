import os


class Config:
    """Base configuration shared by all environments."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret-key")
    
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://flask_user:flask_password@localhost:3306/flask_app_db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configuration for local development."""

    DEBUG = True
    ENV = "development"





class ProductionConfig(Config):
    """Configuration for production deployments."""

    DEBUG = False
    ENV = "production"

