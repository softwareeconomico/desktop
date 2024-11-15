class DataModel:
    """A simple data model representing the entity."""
    def __init__(self, text=""):
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        print(f"DataModel text set to: '{value}'")  # Log every modification
        self._text = value

    def __str__(self):
        return f"DataModel(text={self._text})"