# SecondaryController.py
class SecondaryController:
    """Controller for handling operations in the SecondaryView."""

    def __init__(self, view, repository):
        self.view = view
        self.repository = repository

    def save_data(self, text):
        """Save the data through the repository and update the view."""
        success = self.repository.save_data(text)
        message = "Data saved successfully!" if success else "Failed to save data."
        self.view.update_display(message)  # Update the view with the result

    def clear_data(self):
        """Clear the data using the repository and update the view."""
        self.repository.clear_data()
        self.view.update_display("Data cleared secondary view.")