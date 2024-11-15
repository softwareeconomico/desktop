from app.controllers.secondary_controller import SecondaryController
from app.views.secondary_view import SecondaryView

class MainController:
    """Controller handling interactions between the view and the repository."""

    def __init__(self, main_view, repository):
        self.main_view = main_view
        self.repository = repository

    def save_data(self, text):
        """Save the input text using the repository."""
        self.repository.save_data(text)
        self.main_view.update_display("Data saved!")

    def clear_data(self):
        """Clear the data using the repository and update the view."""
        self.repository.clear_data()
        self.main_view.update_display("Data cleared main view.")

    def open_secondary_window(self):
        """Open the secondary window."""
        # Using the shared repository passed to the MainController
        secondary_view = SecondaryView(parent=self.main_view, controller=None)
        secondary_controller = SecondaryController(secondary_view, self.repository)

        # Set the controller for the secondary view
        secondary_view.controller = secondary_controller

        # Block interaction with the main window while the secondary window is open
        secondary_view.grab_set()
        secondary_view.mainloop()

        # After the secondary window is closed, re-enable interaction with the main window
        secondary_view.grab_release()