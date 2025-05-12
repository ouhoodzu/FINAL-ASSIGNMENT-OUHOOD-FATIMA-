import tkinter as tk
from tkinter import messagebox
import pickle

# ------------------- Data Models -------------------
# User class stores basic user information
class User:
    def __init__(self, username, password, name, email, phone, role):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role

# Ticket class represents a single ticket
class Ticket:
    def __init__(self, ticket_type, event, price, details, available=True):
        self.ticket_type = ticket_type
        self.event = event
        self.price = price
        self.details = details  # NEW: Extra information about the ticket
        self.available = available

# Order class stores a user's ticket booking info
class Order:
    def __init__(self, username, ticket_type, event, price, payment_method, card_name=None, card_number=None):
        self.username = username
        self.ticket_type = ticket_type
        self.event = event
        self.price = price
        self.payment_method = payment_method
        self.card_name = card_name
        self.card_number = card_number

# ------------------- File Operations -------------------
# Load data from file
def load_data(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except:
        return []

# Save data to file
def save_data(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

# Initialize tickets if not already present
def init_tickets():
    tickets = load_data("tickets.pkl")
    if not tickets:
        sample = [
            Ticket("Single-Race Pass", "Abu Dhabi GP", 350, "One-day access to race"),
            Ticket("Weekend Package", "Dubai GP", 800, "3-day access + pit tour"),
            Ticket("Group Discount", "Sharjah GP", 1200, "4 tickets + merch bundle")
        ]
        save_data("tickets.pkl", sample)

# ------------------- GUI -------------------
# Start the GUI window
def start_gui():
    init_tickets()
    root = tk.Tk()
    root.title("Grand Prix Ticket System")

    tk.Label(root, text="🏎️ Welcome to the Ticket Booking System", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Login", width=20, command=lambda: login(root)).pack(pady=5)
    tk.Button(root, text="Register", width=20, command=lambda: register(root)).pack(pady=5)

    root.mainloop()

# ------------------- Register -------------------
# Registration form for new users
def register(root):
    reg = tk.Toplevel(root)
    reg.title("Register")

    entries = {}
    for label in ["Username", "Password", "Name", "Email", "Phone"]:
        tk.Label(reg, text=label).pack()
        entry = tk.Entry(reg, show="*" if label == "Password" else None)
        entry.pack()
        entries[label] = entry

    tk.Label(reg, text="Role").pack()
    role_var = tk.StringVar(value="Customer")
    tk.Radiobutton(reg, text="Customer", variable=role_var, value="Customer").pack()
    tk.Radiobutton(reg, text="Admin", variable=role_var, value="Admin").pack()

    def submit():
        vals = [e.get() for e in entries.values()]
        if not all(vals):
            messagebox.showerror("Error", "All fields required")
            return

        users = load_data("users.pkl")
        if any(u.username == vals[0] for u in users):
            messagebox.showerror("Error", "Username taken")
            return

        user = User(*vals, role_var.get())
        users.append(user)
        save_data("users.pkl", users)
        messagebox.showinfo("Done", "Account created")
        reg.destroy()

    tk.Button(reg, text="Submit", command=submit).pack(pady=10)

# ------------------- Login -------------------
# Login screen for existing users
def login(root):
    win = tk.Toplevel(root)
    win.title("Login")

    tk.Label(win, text="Username").pack()
    user_entry = tk.Entry(win)
    user_entry.pack()
    tk.Label(win, text="Password").pack()
    pass_entry = tk.Entry(win, show="*")
    pass_entry.pack()

    def submit():
        username = user_entry.get()
        password = pass_entry.get()
        users = load_data("users.pkl")
        for u in users:
            if u.username == username and u.password == password:
                win.destroy()
                return admin_dashboard(u) if u.role == "Admin" else customer_dashboard(u)
        messagebox.showerror("Failed", "Invalid credentials")

    tk.Button(win, text="Login", command=submit).pack(pady=10)

# ------------------- Customer Dashboard -------------------
def customer_dashboard(user):
    win = tk.Toplevel()
    win.title(f"Welcome {user.name}")

    tk.Button(win, text="🎟️ View Tickets", command=lambda: view_tickets(win, user)).pack(pady=5)
    tk.Button(win, text="📦 My Orders", command=lambda: manage_orders(win, user)).pack(pady=5)
    tk.Button(win, text="✏️ Update Info", command=lambda: update_info(win, user)).pack(pady=5)
    tk.Button(win, text="🗑️ Delete Account", command=lambda: delete_account(win, user)).pack(pady=5)
    tk.Button(win, text="🚪 Logout", command=win.destroy).pack(pady=10)

# Dashboard for admin user
def admin_dashboard(user):
    win = tk.Toplevel()
    win.title("Admin Dashboard")

    tk.Label(win, text="🛠️ Admin Dashboard", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Button(win, text="📊 Ticket Sales Report", command=lambda: ticket_sales_report(win)).pack(pady=5)
    tk.Button(win, text="👤 View My Info", command=lambda: view_info(win, user)).pack(pady=5)
    tk.Button(win, text="🗑️ Delete My Account", command=lambda: delete_account(win, user)).pack(pady=5)
    tk.Button(win, text="🚪 Logout", command=win.destroy).pack(pady=10)

# Show admin or user info
def view_info(parent, user):
    win = tk.Toplevel(parent)
    win.title("My Info")
    tk.Label(win, text=f"Username: {user.username}").pack()
    tk.Label(win, text=f"Name: {user.name}").pack()
    tk.Label(win, text=f"Email: {user.email}").pack()
    tk.Label(win, text=f"Phone: {user.phone}").pack()
    tk.Label(win, text=f"Role: {user.role}").pack()

# View total ticket sales
def ticket_sales_report(parent):
    win = tk.Toplevel(parent)
    win.title("Ticket Sales Report")

    orders = load_data("orders.pkl")
    summary = {}
    for o in orders:
        key = f"{o.ticket_type} - {o.event}"
        summary[key] = summary.get(key, 0) + 1

    tk.Label(win, text="📊 Ticket Sales Summary", font=("Arial", 14, "bold")).pack(pady=5)
    if not summary:
        tk.Label(win, text="No tickets sold yet.").pack(pady=5)
    else:
        for k, v in summary.items():
            tk.Label(win, text=f"{k}: {v} tickets sold").pack()

# ------------------- View & Book Tickets -------------------
def view_tickets(parent, user):
    win = tk.Toplevel(parent)
    win.title("Available Tickets")
    tickets = load_data("tickets.pkl")
    available = [t for t in tickets if t.available]

    if not available:
        tk.Label(win, text="⚠️ No available tickets at the moment.", font=("Arial", 12, "bold")).pack(padx=20, pady=20)
        return

    selected = tk.IntVar()
    payment = tk.StringVar(value="Cash")

    for i, t in enumerate(available):
        tk.Radiobutton(
            win,
            text=f"{t.ticket_type} - {t.event} - {t.price} AED - {t.details}",
            variable=selected,
            value=i
        ).pack(anchor="w")

    tk.Label(win, text="Select payment method:").pack(pady=(10, 0))
    tk.Radiobutton(win, text="Credit Card", variable=payment, value="Credit").pack()
    tk.Radiobutton(win, text="Digital Wallet", variable=payment, value="Cash").pack()

    tk.Button(
        win,
        text="Confirm Booking",
        command=lambda: confirm_booking(available, selected.get(), user, payment.get(), win)
    ).pack(pady=10)

# Confirm ticket and record order
def confirm_booking(available_tickets, index, user, method, window):
    t = available_tickets[index]
    t.available = False
    all_tickets = load_data("tickets.pkl")

    for i in range(len(all_tickets)):
        if all_tickets[i].ticket_type == t.ticket_type and all_tickets[i].event == t.event:
            all_tickets[i].available = False
            break

    save_data("tickets.pkl", all_tickets)

    orders = load_data("orders.pkl")
    order = Order(user.username, t.ticket_type, t.event, t.price, method)
    orders.append(order)
    save_data("orders.pkl", orders)

    messagebox.showinfo("Success", f"🎉 Booked: {t.ticket_type} for {t.price} AED")
    window.destroy()

# ------------------- Manage Orders -------------------
def manage_orders(parent, user):
    win = tk.Toplevel(parent)
    orders = load_data("orders.pkl")
    user_orders = [o for o in orders if o.username == user.username]

    for i, o in enumerate(user_orders):
        tk.Label(win, text=f"{i+1}. {o.ticket_type} - {o.event} - {o.price} AED").pack()
        if o.payment_method == "Credit":
            tk.Label(win, text=f"Paid by {o.card_name} ({o.card_number})").pack()

    def delete():
        idx = int(entry.get()) - 1
        if 0 <= idx < len(user_orders):
            orders.remove(user_orders[idx])
            save_data("orders.pkl", orders)
            messagebox.showinfo("Deleted", "Order removed")
            win.destroy()

    tk.Label(win, text="Enter order number to delete").pack()
    entry = tk.Entry(win)
    entry.pack()
    tk.Button(win, text="Delete Order", command=delete).pack(pady=5)

# ------------------- Account Management -------------------
def update_info(parent, user):
    win = tk.Toplevel(parent)
    tk.Label(win, text="New Email").pack()
    email = tk.Entry(win)
    email.insert(0, user.email)
    email.pack()
    tk.Label(win, text="New Phone").pack()
    phone = tk.Entry(win)
    phone.insert(0, user.phone)
    phone.pack()

    def update():
        users = load_data("users.pkl")
        for u in users:
            if u.username == user.username:
                u.email = email.get()
                u.phone = phone.get()
        save_data("users.pkl", users)
        messagebox.showinfo("Updated", "Info changed.")
        win.destroy()

    tk.Button(win, text="Save", command=update).pack()

# Delete user account
def delete_account(parent, user):
    users = load_data("users.pkl")
    users = [u for u in users if u.username != user.username]
    save_data("users.pkl", users)
    messagebox.showinfo("Deleted", "Account removed")
    parent.destroy()

# ------------------- Run -------------------
if __name__ == "__main__":
    start_gui()

