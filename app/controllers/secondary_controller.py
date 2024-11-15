# SecondaryController.py
class SecondaryController:
    """Controller for handling operations in the SecondaryView."""

    def __init__(self, view, repository):
        """Initialize the SecondaryController with a view and repository."""
        self.view = view  # The view that this controller will interact with (e.g., SecondaryView)
        self.repository = repository  # The repository that manages the data (e.g., DataRepository)

    def save_data(self, text):
        """Save the data through the repository and update the view."""
        # Validate that the user has entered data
        if not text.strip():  # Check if the text is empty or contains only spaces
            self.view.update_display("Please enter some data before saving.")  # Inform the user
            return  # Exit the function if no data was entered

        # Proceed with saving if data is entered
        success = self.repository.save_data(text)  # Save the data using the repository's save_data method
        # Determine the message based on the result of the save operation
        message = "Data saved successfully!" if success else "Failed to save data."
        self.view.update_display(message)  # Update the view with the result message

    def clear_data(self):
        """Clear the data using the repository and update the view."""
        text = self.view.entry.get()  # Get the data entered by the user
        if not text.strip():  # If no data is entered
            self.view.update_display("No data to clear.")  # Inform the user
            return  # Exit the function if there is no data to clear

        # Proceed with clearing data if there's any entered data
        self.repository.clear_data()  # Clear the data through the repository's clear_data method
        self.view.update_display("Data cleared secondary view.")  # Update the view with the clear operation result
