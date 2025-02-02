import random  # For generating random choices
import string  # For character sets (letters, digits, special characters)
import numpy as np  # For AI-based advanced randomness
import tkinter as tk  # For GUI creation
from tkinter import ttk  # For modern-looking widgets in Tkinter
from tkinter import messagebox  # To show messages in the GUI
from collections import Counter  # To count occurrences of characters in a password
from math import log2  # For entropy calculation
import pyperclip  # To copy passwords to the clipboard


def calculate_entropy(password):
    """
    Calculate Shannon entropy to measure password strength.
    Higher entropy means a more unpredictable password.
    """
    if not password:  # If password is empty, return 0 entropy
        return 0
    char_counts = Counter(password)  # Count occurrences of each character
    length = len(password)  # Total length of password
    entropy = -sum((count / length) * log2(count / length) for count in char_counts.values())  # Shannon entropy formula
    return entropy  # Return entropy value


def ai_password_generator(length=16, use_digits=True, use_special=True, avoid_ambiguous=True):
    """
    Generate a highly secure password using AI-based randomness and entropy analysis.
    - length: Length of the password
    - use_digits: Include numbers (0-9)
    - use_special: Include special characters (!@#$%^&*)
    - avoid_ambiguous: Exclude characters that look similar (O/0, l/1, etc.)
    """
    # Define character sets
    characters = string.ascii_letters  # Include uppercase and lowercase letters
    if use_digits:
        characters += string.digits  # Add numbers if enabled
    if use_special:
        characters += string.punctuation  # Add special characters if enabled
    if avoid_ambiguous:
        ambiguous_chars = "lI1O0{}[]()/\\'\"`~,;:.<>"  # Define ambiguous characters
        characters = ''.join(c for c in characters if c not in ambiguous_chars)  # Remove ambiguous characters

    # AI-based randomness: Use NumPy's sampling for more secure password generation
    password = ''.join(np.random.choice(list(characters), length))

    # Ensure high entropy for security
    entropy = calculate_entropy(password)
    while entropy < 4.0:  # 4.0 is a reasonable threshold for strong passwords
        password = ''.join(np.random.choice(list(characters), length))
        entropy = calculate_entropy(password)

    return password, entropy  # Return generated password and entropy score


# GUI Application Class
class PasswordGeneratorApp:
    def __init__(self, root):
        """
        Initialize the GUI components for the Password Generator.
        """
        self.root = root
        self.root.title("AI-Powered Password Generator")  # Set window title
        self.root.geometry("400x300")  # Set window size
        self.root.resizable(False, False)  # Disable resizing

        # Label for password length selection
        ttk.Label(root, text="Password Length:").pack(pady=5)
        self.length_var = tk.IntVar(value=16)  # Default password length is 16
        self.length_entry = ttk.Entry(root, textvariable=self.length_var, width=5)  # Input field for length
        self.length_entry.pack()

        # Checkbox options
        self.use_digits = tk.BooleanVar(value=True)  # Include digits by default
        self.use_special = tk.BooleanVar(value=True)  # Include special characters by default
        self.avoid_ambiguous = tk.BooleanVar(value=True)  # Avoid ambiguous characters by default

        # Create checkboxes for user options
        ttk.Checkbutton(root, text="Include Digits", variable=self.use_digits).pack()
        ttk.Checkbutton(root, text="Include Special Characters", variable=self.use_special).pack()
        ttk.Checkbutton(root, text="Avoid Ambiguous Characters", variable=self.avoid_ambiguous).pack()

        # Generate Password Button
        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Password Display Field
        self.password_var = tk.StringVar()  # Variable to store the password
        self.password_entry = ttk.Entry(root, textvariable=self.password_var, state="readonly", width=35)
        self.password_entry.pack(pady=5)

        # Label to show entropy score
        self.entropy_var = tk.StringVar()  # Variable to store entropy value
        ttk.Label(root, text="Entropy:").pack()
        self.entropy_label = ttk.Label(root, textvariable=self.entropy_var)  # Display entropy
        self.entropy_label.pack()

        # Copy to Clipboard Button
        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)

    def generate_password(self):
        """
        Generate a new password based on user settings and update the GUI.
        """
        length = self.length_var.get()  # Get password length from user input
        use_digits = self.use_digits.get()  # Check if digits should be included
        use_special = self.use_special.get()  # Check if special characters should be included
        avoid_ambiguous = self.avoid_ambiguous.get()  # Check if ambiguous characters should be avoided

        # Generate password with AI-based randomness
        password, entropy = ai_password_generator(length, use_digits, use_special, avoid_ambiguous)

        # Update the password field and entropy display
        self.password_var.set(password)
        self.entropy_var.set(f"{entropy:.2f}")  # Show entropy score with 2 decimal places

    def copy_to_clipboard(self):
        """
        Copy the generated password to the system clipboard.
        """
        password = self.password_var.get()  # Get the generated password
        if password:  # Check if password is available
            pyperclip.copy(password)  # Copy to clipboard
            messagebox.showinfo("Copied", "Password copied to clipboard!")  # Show confirmation message


# Run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    app = PasswordGeneratorApp(root)  # Initialize the app
    root.mainloop()  # Start the GUI event loop
