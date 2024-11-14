# settings.py

from config.config import DevelopmentConfig

# The global configuration is determined based on the environment
# In this case, use `DevelopmentConfig` for development and `ProductionConfig` for production
CONFIG = DevelopmentConfig  # Switch to ProductionConfig in production environments

# File path configuration
FILE_PATHS = {
    "log": "logs/",   # Path for the log files
    "uploads": "uploads/"  # Path for uploaded files
}

# External API configuration (e.g. keys for external services)
EXTERNAL_API = {
    "service_1": "my_api_key_service_1",  # API key for service 1
    "service_2": "my_api_key_service_2"   # API key for service 2
}