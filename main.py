import pickle
from classes import *  # Import all model classes from classes.py


# Save data to a .pkl file
def save_data(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


# Load data from a .pkl file
def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file does not exist


# Load all data when the program starts
users = load_data("users.pkl")
tickets = load_data("tickets.pkl")
orders = load_data("orders.pkl")
sales = load_data("sales.pkl")


# Add default admin user if users list is empty
if not users:
    admin = Admin("admin1", "adminpass", "Admin User", "A001", "Manager")
    users.append(admin)
    save_data("users.pkl", users)


# Entry point for running the program
def main():
    print("System ready. GUI will launch here later.")


if __name__ == "__main__":
    main()

