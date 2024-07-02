import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length, include_uppercase, include_digits, include_special):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    if len(characters) == 0:
        messagebox.showerror("Error", "Select at least one option for complexity.")
        return ""

    password = ''.join(random.choices(characters, k=length))
    return password

def generate_password_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than zero.")
            return
        
        include_uppercase = uppercase_var.get()
        include_digits = digits_var.get()
        include_special = special_var.get()

        password = generate_password(length, include_uppercase, include_digits, include_special)
        if password:
            password_label.config(text=f"Generated Password: {password}")
            copy_button.config(state=tk.NORMAL)  # Enable the copy button
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

def copy_password():
    password = password_label.cget("text")
    if password.startswith("Generated Password: "):
        password = password[len("Generated Password: "):]  # Remove the label text
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create GUI elements
length_label = tk.Label(window, text="Enter the desired length of the password:")
length_label.pack(pady=10)

length_entry = tk.Entry(window, width=30)
length_entry.pack()

complexity_frame = tk.LabelFrame(window, text="Complexity Options:")
complexity_frame.pack(pady=10)

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(complexity_frame, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack(anchor=tk.W)

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(complexity_frame, text="Include Digits (0-9)", variable=digits_var)
digits_check.pack(anchor=tk.W)

special_var = tk.BooleanVar()
special_check = tk.Checkbutton(complexity_frame, text="Include Special Characters (!@#$%^&*)", variable=special_var)
special_check.pack(anchor=tk.W)

generate_button = tk.Button(window, text="Generate Password", command=generate_password_button_clicked)
generate_button.pack(pady=10)

password_label = tk.Label(window, text="")
password_label.pack(pady=10)

copy_button = tk.Button(window, text="Copy Password", command=copy_password, state=tk.DISABLED)
copy_button.pack(pady=10)

# Run the main loop
window.mainloop()
