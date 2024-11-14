class DependencyInjector:
    """A simple dependency injector to manage application dependencies."""

    def __init__(self):
        # Dictionary to store registered dependencies
        self._dependencies = {}

    def register(self, name, dependency):
        """Register a new dependency by name."""
        self._dependencies[name] = dependency

    def get(self, name):
        """Retrieve a dependency by name."""
        return self._dependencies.get(name)

    def clear(self):
        """Clear all registered dependencies."""
        self._dependencies.clear()