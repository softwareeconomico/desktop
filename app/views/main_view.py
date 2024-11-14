# MainView.py
import customtkinter as ctk
from PIL import Image
from app.views.secondary_view import SecondaryView
from app.controllers.secondary_controller import SecondaryController
from app.repositories.data_repository import DataRepository
import sys

class MainView(ctk.CTk):
    """Main application view with a text entry and buttons."""

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Data Entry Application")

        # Set window size and center it
        self.geometry("800x600")
        self.update_idletasks()
        window_width = 800
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Set the window icon
        self.iconbitmap("assets/icon.ico")

        # Load and display logo image
        self.logo_image = ctk.CTkImage(Image.open("assets/logo.png"), size=(200, 200))
        self.logo_label = ctk.CTkLabel(self, image=self.logo_image, text="")
        self.logo_label.pack(pady=20)

        # Label, Entry, Save, Clear buttons
        self.label = ctk.CTkLabel(self, text="Enter some text:")
        self.label.pack(pady=10)
        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=10, fill=ctk.X, padx=20)
        self.save_button = ctk.CTkButton(self, text="Save Data", command=self.save_data)
        self.save_button.pack(pady=10)
        self.clear_button = ctk.CTkButton(self, text="Clear Data", command=self.clear_data)
        self.clear_button.pack(pady=10)

        # Open New Window button
        self.open_window_button = ctk.CTkButton(self, text="Open New Window", command=self.controller.open_secondary_window)
        self.open_window_button.pack(pady=10)

        # Additional Close Application button
        self.close_app_button = ctk.CTkButton(self, text="Close Application", command=self.on_close)
        self.close_app_button.pack(pady=10)

        # Message label for feedback
        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.pack(pady=20)

        # Set the close event to terminate the program
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def save_data(self):
        """Handle save button click."""
        text = self.entry.get()
        self.controller.save_data(text)

    def clear_data(self):
        """Handle clear button click."""
        self.controller.clear_data()
        self.entry.delete(0, ctk.END)

    def update_display(self, message):
        """Update the message display in the view."""
        self.message_label.configure(text=message)

    def on_close(self):
        """Terminate the program when the main window is closed."""
        self.destroy()
        sys.exit()
