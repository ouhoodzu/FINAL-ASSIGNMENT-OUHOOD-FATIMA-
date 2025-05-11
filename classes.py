# classes.py
# The base class for all users (both customers and admins).
# It handles the most basic user information: username and password.
class User:
   def __init__(self, username, password):
       # Private attributes for login credentials
       self.__username = username
       self.__password = password
 
   # Get the username (used for login, display, etc.)
   def getUsername(self):
       return self.__username
 
   # Set/change the username
   def setUsername(self, username):
       self.__username = username
 
   # Get the password (used for login verification)
   def getPassword(self):
       return self.__password
 
   # Set/change the password
   def setPassword(self, password):
       self.__password = password
 
 
 
# Customer Class (Inherits User)
# The Customer class represents a user who can book tickets.
# Inherits login data from User and adds personal details (name, email, phone).
class Customer(User):
   def __init__(self, username, password, name, email, phone_number):
       super().__init__(username, password)
       self.__name = name  # Full name of the customer
       self.__email = email  # Email for communication
       self.__phone_number = phone_number  # Phone number for contact
 
   # Get and set name
   def getName(self):
       return self.__name
 
   def setName(self, name):
       self.__name = name
 
   # Get and set email
   def getEmail(self):
       return self.__email
 
   def setEmail(self, email):
       self.__email = email
 
   # Get and set phone number
   def getPhoneNumber(self):
       return self.__phone_number
 
   def setPhoneNumber(self, phone_number):
       self.__phone_number = phone_number
 
# Admin Class (Inherits User)
 
# The Admin class represents a user with elevated permissions.
# Admins can apply discounts, view sales reports, etc.
class Admin(User):
   def __init__(self, username, password, name, admin_id, role):
# Call the parent class constructor
       super().__init__(username, password)
       self.__name = name
       self.__admin_id = admin_id  # Unique ID for admin
       self.__role = role  # Role can be "manager", "coordinator", etc.
 
   def getName(self):
       return self.__name
 
   def setName(self, name):
       self.__name = name
 
   def getAdminID(self):
       return self.__admin_id
 
   def setAdminID(self, admin_id):
       self.__admin_id = admin_id
 
   def getRole(self):
       return self.__role
 
 
# Ticket Class (Base Class)
# The base class for all types of tickets.
# Shared attributes: event info, seat info, availability, price.
class Ticket:
   def __init__(self, ticket_id, ticket_type, price, event_date, event_name, seat_number, gate_entry, is_available):
       self.__ticket_id = ticket_id  # Unique ID for each ticket
       self.__ticket_type = ticket_type  # e.g., "Single", "Weekend", "Group"
       self.__price = price  # Ticket price in AED
       self.__event_date = event_date  # Date of the race/event
       self.__event_name = event_name  # Name of the race/event
       self.__seat_number = seat_number  # Seat assigned to ticket
       self.__gate_entry = gate_entry  # Which gate to enter from
       self.__is_available = is_available  # True if still bookable
 
   # Getters and setters for all ticket attributes
   def getTicketID(self): return self.__ticket_id
   def setTicketID(self, ticket_id): self.__ticket_id = ticket_id
 
   def getTicketType(self): return self.__ticket_type
   def setTicketType(self, ticket_type): self.__ticket_type = ticket_type
 
   def getPrice(self): return self.__price
   def setPrice(self, price): self.__price = price
 
   def getEventDate(self): return self.__event_date
   def setEventDate(self, event_date): self.__event_date = event_date
 
   def getEventName(self): return self.__event_name
   def setEventName(self, event_name): self.__event_name = event_name
 
   def getSeatNumber(self): return self.__seat_number
   def setSeatNumber(self, seat_number): self.__seat_number = seat_number
 
   def getGateEntry(self): return self.__gate_entry
   def setGateEntry(self, gate_entry): self.__gate_entry = gate_entry
 
   def getIsAvailable(self): return self.__is_available
   def setIsAvailable(self, is_available): self.__is_available = is_available
 
# SinglePassTicket Class (Inherits Ticket)
# Single-pass ticket for one-time event use
class SinglePassTicket(Ticket):
   def __init__(self, ticket_id, price, event_date, event_name, seat_number, gate_entry, is_available):
       # Set ticket_type to "Single"
WeekendPackageTicket Class (Inherits Ticket)
# Weekend package including hotel stay or meals
 
class WeekendPackageTicket(Ticket):
   def __init__(self, ticket_id, price, event_date, event_name, seat_number, gate_entry, is_available, includes_meals, hotel_name):
def displayWeekendPackage(self):
       return f"Weekend Package - Hotel: {self.__hotel_name} | Meals Included: {self.__includes_meals}"
 
# GroupTicket Class (Inherits Ticket)
# Ticket for multiple users with seat group and discounts
 
class GroupTicket(Ticket):
   def __init__(self, ticket_id, price, event_date, event_name, seat_numbers, gate_entry, is_available, group_size, discount_rate):
 
# Booking Class
# Booking details for a confirmed or pending reservation
class Booking:
   def __init__(self, booking_date, is_confirmed):
       # Private attributes for booking details
 
 
# BookingHistory Class
# History record for storing booking logs (can be used for admin reports)
 
class BookingHistory:
   def __init__(self, booking_id, user_id, ticket_id, booking_date):
 
# CreditCardPayment Class (Inherits Payment)
# Credit card-specific payment info (used in secure online payment forms)
 
class CreditCardPayment(Payment):
   def __init__(self, payment_id, amount, payment_date, card_number, card_holder_name, expiry_date):
# CashPayment Class (Inherits Payment)
# Cash payment handling with amount given and change
class CashPayment(Payment):
   def __init__(self, payment_id, amount, payment_date, cash_amount, change):
       # Call parent constructor with method set to "Cash"
