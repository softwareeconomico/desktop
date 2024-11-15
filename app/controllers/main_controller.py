from app.controllers.secondary_controller import SecondaryController
from app.views.secondary_view import SecondaryView

class MainController:
    """Controller handling interactions between the view and the repository."""

    def __init__(self, main_view, repository):
        self.main_view = main_view  # The view that displays the interface
        self.repository = repository  # The repository that handles data storage

    def save_data(self, text):
        """Save the input text using the repository."""
        print(f"Before save, model data is: '{self.repository.get_data()}'")
        self.repository.save_data(text)
        print(f"After save, model data is: '{self.repository.get_data()}'")

    def clear_data(self):
        """Clear the data using the repository and update the view."""
        print("Checking if data exists in clear_data()...")
        print(f"Current data in model before clearing: '{self.repository.get_data()}'")
        if not self.repository.has_data():
            self.main_view.update_display("Error: No data to clear.")
        else:
            self.repository.clear_data()
            print("Data cleared.")
            print(f"Current data in model after clearing: '{self.repository.get_data()}'")
            self.main_view.update_display("Data cleared.")

    def open_secondary_window(self):
        """Open the secondary window."""
        # Open the secondary view, passing the shared repository to the secondary controller
        secondary_view = SecondaryView(parent=self.main_view, controller=None)
        secondary_controller = SecondaryController(secondary_view, self.repository)

        # Set the controller for the secondary window
        secondary_view.controller = secondary_controller

        # Block interaction with the main window while the secondary window is open
        secondary_view.grab_set()
        secondary_view.mainloop()

        # After the secondary window is closed, re-enable interaction with the main window
        secondary_view.grab_release()