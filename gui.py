# gui.py

import tkinter as tk
from tkinter import messagebox
import pickle
from classes import *

# Load user data from pickle file
def load_users():
    try:
        with open("users.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Save user data to pickle file
def save_users(users):
    with open("users.pkl", "wb") as file:
        pickle.dump(users, file)


# Register New Customer

def register():
    def submit_registration():
        username = entry_username.get()
        password = entry_password.get()
        name = entry_name.get()
        email = entry_email.get()
        phone = entry_phone.get()

        users = load_users()

        # Check if username already exists
        for user in users:
            if user.getUsername() == username:
                messagebox.showerror("Error", "Username already exists")
                return

        # Create new customer and save
        new_customer = Customer(username, password, name, email, phone)
        users.append(new_customer)
        save_users(users)

        messagebox.showinfo("Success", "Account created successfully!")
        register_window.destroy()

    # Create registration form
    register_window = tk.Toplevel()
    register_window.title("Register")

    tk.Label(register_window, text="Username").pack()
    entry_username = tk.Entry(register_window)
    entry_username.pack()

    tk.Label(register_window, text="Password").pack()
    entry_password = tk.Entry(register_window, show="*")
    entry_password.pack()

    tk.Label(register_window, text="Name").pack()
    entry_name = tk.Entry(register_window)
    entry_name.pack()

    tk.Label(register_window, text="Email").pack()
    entry_email = tk.Entry(register_window)
    entry_email.pack()

    tk.Label(register_window, text="Phone").pack()
    entry_phone = tk.Entry(register_window)
    entry_phone.pack()

    tk.Button(register_window, text="Submit", command=submit_registration).pack()


# Login Screen

def login():
    def process_login():
        username = entry_username.get()
        password = entry_password.get()
        users = load_users()

        for user in users:
            if user.getUsername() == username and user.getPassword() == password:
                messagebox.showinfo("Login Success", f"Welcome, {username}!")
                login_window.destroy()
                if isinstance(user, Admin):
                    launch_admin_panel()
                else:
                    launch_customer_panel(user)
                return

        messagebox.showerror("Login Failed", "Invalid username or password")

    # Create login form
    login_window = tk.Toplevel()
    login_window.title("Login")

    tk.Label(login_window, text="Username").pack()
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    tk.Label(login_window, text="Password").pack()
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack()

    tk.Button(login_window, text="Login", command=process_login).pack()


# Placeholder Panels (To be built later)

def launch_customer_panel(user):
    messagebox.showinfo("Customer", "Customer panel coming soon!")

def launch_admin_panel():
    messagebox.showinfo("Admin", "Admin panel coming soon!")


# Main GUI Window

def start_gui():
    window = tk.Tk()
    window.title("Grand Prix Experience")

    tk.Label(window, text="Welcome to the Ticket System", font=("Arial", 16)).pack(pady=10)

    tk.Button(window, text="Login", width=20, command=login).pack(pady=5)
    tk.Button(window, text="Register", width=20, command=register).pack(pady=5)

    window.mainloop()
