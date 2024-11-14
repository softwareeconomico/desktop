class DataModel:
    """A simple data model representing the entity."""
    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return f"DataModel(text={self.text})"