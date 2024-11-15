from app.models.data_model import DataModel

class DataRepository:
    """Repository managing the DataModel instance."""

    def __init__(self):
        self.data_model = DataModel()

    def save_data(self, text):
        """Save data by updating the data model's text attribute."""
        if text:
            self.data_model.text = text
            print(f"Data saved successfully: '{self.data_model.text}'")
        else:
            print("Attempted to save empty data.")

    def clear_data(self):
        """Clear the data in the model."""
        self.data_model.text = ""
        print("Data cleared in model.")

    def get_data(self):
        """Retrieve the current data."""
        return self.data_model.text

    def has_data(self):
        """Check if there is any data to clear."""
        current_data = self.data_model.text.strip()
        print(f"Checking data in has_data(): '{current_data}'")  # Debug statement
        return bool(current_data)  # Returns True if text is not empty