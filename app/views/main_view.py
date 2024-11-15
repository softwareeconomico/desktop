# MainView.py
import sys
import customtkinter as ctk
from PIL import Image

import customtkinter as ctk
from PIL import Image
import sys

import customtkinter as ctk
from PIL import Image
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

        # Create the logo label and adjust its size dynamically based on window size
        self.logo_label = ctk.CTkLabel(self, text="", anchor="center")
        self.logo_label.grid(row=0, column=0, columnspan=3, pady=20, sticky="nsew")

        # Update the logo size based on the window size
        self.after(100, self.update_logo)

        # Label, Entry, Save, Clear buttons
        self.label = ctk.CTkLabel(self, text="Enter some text:")
        self.label.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky="w")

        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Load icons for buttons
        save_icon = ctk.CTkImage(Image.open("assets/add.png"), size=(20, 20))
        clear_icon = ctk.CTkImage(Image.open("assets/check.png"), size=(20, 20))
        open_window_icon = ctk.CTkImage(Image.open("assets/list-option.png"), size=(20, 20))
        close_app_icon = ctk.CTkImage(Image.open("assets/right.png"), size=(20, 20))

        # Save Data button with icon
        self.save_button = ctk.CTkButton(self, text="Save", image=save_icon, compound="left", command=self.save_data)
        self.save_button.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Clear Data button with icon
        self.clear_button = ctk.CTkButton(self, text="Clear", image=clear_icon, compound="left", command=self.clear_data)
        self.clear_button.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Open New Window button with icon
        self.open_window_button = ctk.CTkButton(self, text="Open", image=open_window_icon, compound="left", command=self.controller.open_secondary_window)
        self.open_window_button.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Close Application button with icon
        self.close_app_button = ctk.CTkButton(self, text="Close", image=close_app_icon, compound="left", command=self.on_close)
        self.close_app_button.grid(row=6, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        # Message label for feedback
        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.grid(row=7, column=0, columnspan=3, pady=20, sticky="ew")

        # Configure rows and columns to be expandable
        self.grid_rowconfigure(0, weight=1)  # Logo row
        self.grid_rowconfigure(1, weight=0)  # Label row
        self.grid_rowconfigure(2, weight=0)  # Entry row
        self.grid_rowconfigure(3, weight=0)  # Save button row
        self.grid_rowconfigure(4, weight=0)  # Clear button row
        self.grid_rowconfigure(5, weight=0)  # Open New Window row
        self.grid_rowconfigure(6, weight=0)  # Close Application row
        self.grid_rowconfigure(7, weight=1)  # Message row

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

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

    def update_logo(self):
        """Adjust the logo size based on window size."""
        window_width = self.winfo_width()
        logo_size = int(window_width * 0.25)  # 25% of the window width
        self.logo_image = ctk.CTkImage(Image.open("assets/logo.png"), size=(logo_size, logo_size))
        self.logo_label.configure(image=self.logo_image)
        self.logo_label.image = self.logo_image  # Keep reference to avoid garbage collection
        self.after(100, self.update_logo)  # Update the logo size every 100ms
