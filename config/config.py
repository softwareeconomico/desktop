# config.py

class Config:
    """General configuration for the application"""

    ENV = "development"  # The environment in which the app is running ('development' or 'production')
    DEBUG = True  # Enables debugging mode
    SECRET_KEY = "mysecretkey"  # Secret key used for app security (e.g. sessions, cookies)

    # Database configuration
    DATABASE = {
        "host": "localhost",  # Database host
        "port": 5432,  # Database port
        "user": "myuser",  # Database user
        "password": "mypassword",  # Database password
        "db": "mydatabase"  # Database name
    }

    # Logging configuration
    LOGGING = {
        "level": "DEBUG",  # The log level ('DEBUG', 'INFO', 'WARNING', etc.)
        "file": "app.log"  # The log file location
    }


# Configuration for the app in development
class DevelopmentConfig(Config):
    ENV = "development"  # Set the environment to development
    DEBUG = True  # Enable debugging in development