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
        self.logo_label.grid(row=0, column=0, columnspan=3, pady=20, sticky="nsew")

        # Create a label and entry field for this secondary window
        self.label = ctk.CTkLabel(self, text="Enter some more text:")
        self.label.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky="w")

        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Load icons for the buttons
        save_icon = ctk.CTkImage(Image.open("assets/add.png"), size=(20, 20))  # Replace with your icon path
        clear_icon = ctk.CTkImage(Image.open("assets/check.png"), size=(20, 20))  # Replace with your icon path
        close_icon = ctk.CTkImage(Image.open("assets/right.png"), size=(20, 20))  # Replace with your icon path

        # Save button with icon
        self.save_button = ctk.CTkButton(self, text="Save", image=save_icon, compound="left", command=self.save_data)
        self.save_button.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Clear button with icon
        self.clear_button = ctk.CTkButton(self, text="Clear", image=clear_icon, compound="left", command=self.clear_data)
        self.clear_button.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Close button with icon
        self.close_button = ctk.CTkButton(self, text="Close", image=close_icon, compound="left", command=self.close_window)
        self.close_button.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Configure rows and columns to be expandable
        self.grid_rowconfigure(0, weight=1)  # Logo row
        self.grid_rowconfigure(1, weight=0)  # Label row
        self.grid_rowconfigure(2, weight=0)  # Entry row
        self.grid_rowconfigure(3, weight=0)  # Save button row
        self.grid_rowconfigure(4, weight=0)  # Clear button row
        self.grid_rowconfigure(5, weight=0)  # Close button row

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

        # Center the secondary window relative to the parent window
        self.center_window(parent)

        # Update the logo size whenever the window is resized
        self.after(100, self.update_logo)

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

    def update_logo(self):
        """Adjust the logo size based on window size."""
        window_width = self.winfo_width()
        logo_size = int(window_width * 0.20)  # 20% of the window width
        self.logo_image = ctk.CTkImage(Image.open("assets/logo.png"), size=(logo_size, logo_size))
        self.logo_label.configure(image=self.logo_image)
        self.after(100, self.update_logo)  # Update the logo size every 100ms

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