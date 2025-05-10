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

        # Create and save new customer
        new_customer = Customer(username, password, name, email, phone)
        users.append(new_customer)
        save_users(users)

        messagebox.showinfo("Success", "Account created successfully!")
        register_window.destroy()

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

    login_window = tk.Toplevel()
    login_window.title("Login")

    tk.Label(login_window, text="Username").pack()
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    tk.Label(login_window, text="Password").pack()
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack()

    tk.Button(login_window, text="Login", command=process_login).pack()

# Customer Panel After Login
def launch_customer_panel(user):
    customer_window = tk.Toplevel()
    customer_window.title(f"Welcome, {user.getName()}")

    tk.Label(customer_window, text=f"Welcome {user.getName()}", font=("Arial", 14)).pack(pady=10)

    tk.Button(customer_window, text="View Available Tickets", width=30, command=view_tickets).pack(pady=5)
    tk.Button(customer_window, text="Book a Ticket", width=30, command=lambda: book_ticket(user)).pack(pady=5)
    tk.Button(customer_window, text="View My Bookings", width=30, command=lambda: view_booking_history(user)).pack(pady=5)
    tk.Button(customer_window, text="Logout", width=30, command=customer_window.destroy).pack(pady=10)

# View Available Tickets
def view_tickets():
    try:
        with open("tickets.pkl", "rb") as file:
            tickets = pickle.load(file)
    except FileNotFoundError:
        messagebox.showinfo("No Tickets", "No tickets found.")
        return

    ticket_window = tk.Toplevel()
    ticket_window.title("Available Tickets")

    if not tickets:
        tk.Label(ticket_window, text="No tickets available.").pack()
        return

    canvas = tk.Canvas(ticket_window, width=400, height=300)
    frame = tk.Frame(canvas)
    scrollbar = tk.Scrollbar(ticket_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    for ticket in tickets:
        info = f"Type: {ticket.getTicketType()} | Event: {ticket.getEventName()} | Seat: {ticket.getSeatNumber()} | Price: {ticket.getPrice()} AED | Available: {'Yes' if ticket.getIsAvailable() else 'No'}"
        tk.Label(frame, text=info, anchor="w", justify="left").pack(padx=10, pady=5)

# Admin Panel Placeholder (build later)
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
