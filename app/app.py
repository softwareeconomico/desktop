from app.managers.dependency_injector import DependencyInjector
from app.repositories.data_repository import DataRepository
from app.controllers.main_controller import MainController
from app.views.main_view import MainView

class App:
    """Main application class to initialize and run the app with Dependency Injection."""

    def __init__(self, config=None):
        # Optionally, handle the config here (e.g., save it or apply it)
        self.config = config

        # Initialize the Dependency Injector
        self.injector = DependencyInjector()

        # Register dependencies
        self._register_dependencies()

        # Initialize main components
        self.main_view = self.injector.get("main_view")
        self.main_controller = self.injector.get("main_controller")

    def _register_dependencies(self):
        """Register dependencies into the Dependency Injector."""

        # Create the repository
        data_repository = DataRepository()
        self.injector.register("data_repository", data_repository)

        # Create the controller first, with no view yet
        main_controller = MainController(None, data_repository)  # Create without a view

        # Create the view and assign the controller to it
        main_view = MainView(controller=main_controller)  # Pass controller to view
        self.injector.register("main_view", main_view)

        # Now, set the controller to the view
        main_controller.main_view = main_view  # Assign the view to the controller

        # Register the controller
        self.injector.register("main_controller", main_controller)

    def run(self):
        """Run the main event loop of the application."""
        self.main_view.mainloop()
