# SecondaryView.py
import os

import customtkinter as ctk
from PIL import Image

# Set the appearance mode and color theme for the application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class SecondaryView(ctk.CTkToplevel):
    """Secondary window view that will be opened from the main window."""

    def __init__(self, parent):
        super().__init__(parent)  # Pass parent to make this window a child of the main window
        self.title("Secondary Window")

        # Set window size for the secondary window, increase the size for better visibility
        self.geometry("500x400")

        # Load and display logo image for the secondary window
        self.logo_image = ctk.CTkImage(Image.open("assets/dashboard.png"), size=(100, 100))  # Adjust the size as needed
        self.logo_label = ctk.CTkLabel(self, image=self.logo_image, text="")
        self.logo_label.pack(pady=20)

        # Center the secondary window relative to the parent window
        self.center_window(parent)

        # Create a label and entry field for this secondary window
        self.label = ctk.CTkLabel(self, text="Enter some more text:")
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=10, fill=ctk.X, padx=20)

        # Save button for the secondary window
        self.save_button = ctk.CTkButton(self, text="Save Data", command=self.save_data)
        self.save_button.pack(pady=10)

        # Clear button to clear the text entry field
        self.clear_button = ctk.CTkButton(self, text="Clear", command=self.clear_data)
        self.clear_button.pack(pady=10)

        # Close button to close the secondary window
        self.close_button = ctk.CTkButton(self, text="Close", command=self.close_window)
        self.close_button.pack(pady=10)

    def center_window(self, parent):
        """Center the secondary window with respect to its parent."""
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()

        # Calculate the position to center the window
        position_top = int(parent_y + (parent_height / 2) - 200)  # Adjust the 200 based on window height
        position_right = int(parent_x + (parent_width / 2) - 250)  # Adjust the 250 based on window width

        self.geometry(f"500x400+{position_right}+{position_top}")  # Position the window with the calculated coordinates

    def save_data(self):
        """Handle save button click in the secondary window."""
        text = self.entry.get()
        # Here you would likely want to send this data somewhere
        print(f"Saved: {text}")

    def clear_data(self):
        """Clear the text entry field."""
        self.entry.delete(0, ctk.END)

    def close_window(self):
        """Close the secondary window."""
        self.destroy()