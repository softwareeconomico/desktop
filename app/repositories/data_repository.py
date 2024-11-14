from app.models.data_model import DataModel

class DataRepository:
    """Repository managing the DataModel instance."""

    def __init__(self):
        self.data_model = DataModel()

    def save_data(self, text):
        """Save data by updating the data model's text attribute."""
        self.data_model.text = text
        print(f"Data saved: {self.data_model}")

    def clear_data(self):
        """Clear the data in the model."""
        self.data_model.text = ""
        print("Data cleared.")

    def get_data(self):
        """Retrieve the current data."""
        return self.data_model.text