# main.py
from config.settings import CONFIG  # Import configuration settings
from app.app import App  # Import the main App class

def create_app():
    # Initialize the application with global settings
    app = App(config=CONFIG)  # Pass configuration to the app
    return app

if __name__ == "__main__":
    # Run the app instance created by create_app
    application = create_app()
    application.run()