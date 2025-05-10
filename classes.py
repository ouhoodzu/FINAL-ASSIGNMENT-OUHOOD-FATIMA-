# classes.py


# User Class (Base Class)

class User:
    def __init__(self, username, password):
        # Private attributes
        self.__username = username
        self.__password = password

    # Getter and setter for username
    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    # Getter and setter for password
    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password



# Customer Class (Inherits User)

class Customer(User):
    def __init__(self, username, password, name, email, phone_number):
        # Call the parent class constructor
        super().__init__(username, password)
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

    # Getter and setter for name
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # Getter and setter for email
    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    # Getter and setter for phone number
    def getPhoneNumber(self):
        return self.__phone_number

    def setPhoneNumber(self, phone_number):
        self.__phone_number = phone_number



# Admin Class (Inherits User)

class Admin(User):
    def __init__(self, username, password, name, admin_id, role):
        # Call the parent class constructor
        super().__init__(username, password)
        self.__name = name
        self.__admin_id = admin_id
        self.__role = role

    # Getter and setter for name
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # Getter and setter for admin ID
    def getAdminID(self):
        return self.__admin_id

    def setAdminID(self, admin_id):
        self.__admin_id = admin_id

    # Getter and setter for role
    def getRole(self):
        return self.__role

    def setRole(self, role):
        self.__role = role


# Ticket Class (Base Class)

class Ticket:
    def __init__(self, ticket_id, ticket_type, price, event_date, event_name, seat_number, gate_entry, is_available):
        # Ticket details shared by all types
        self.__ticket_id = ticket_id
        self.__ticket_type = ticket_type
        self.__price = price
        self.__event_date = event_date
        self.__event_name = event_name
        self.__seat_number = seat_number
        self.__gate_entry = gate_entry
        self.__is_available = is_available

    # Getters and setters for each attribute

    def getTicketID(self):
        return self.__ticket_id

    def setTicketID(self, ticket_id):
        self.__ticket_id = ticket_id

    def getTicketType(self):
        return self.__ticket_type

    def setTicketType(self, ticket_type):
        self.__ticket_type = ticket_type

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def getEventDate(self):
        return self.__event_date

    def setEventDate(self, event_date):
        self.__event_date = event_date

    def getEventName(self):
        return self.__event_name

    def setEventName(self, event_name):
        self.__event_name = event_name

    def getSeatNumber(self):
        return self.__seat_number

    def setSeatNumber(self, seat_number):
        self.__seat_number = seat_number

    def getGateEntry(self):
        return self.__gate_entry

    def setGateEntry(self, gate_entry):
        self.__gate_entry = gate_entry

    def getIsAvailable(self):
        return self.__is_available

    def setIsAvailable(self, is_available):
        self.__is_available = is_available


# SinglePassTicket Class (Inherits Ticket)

class SinglePassTicket(Ticket):
    def __init__(self, ticket_id, price, event_date, event_name, seat_number, gate_entry, is_available):
        # Set ticket_type to "Single"
        super().__init__(ticket_id, "Single", price, event_date, event_name, seat_number, gate_entry, is_available)

    def displaySinglePass(self):
        # Display simple ticket info
        return f"Single Pass - Event: {self.getEventName()} | Seat: {self.getSeatNumber()} | Price: {self.getPrice()}"


# WeekendPackageTicket Class (Inherits Ticket)

class WeekendPackageTicket(Ticket):
    def __init__(self, ticket_id, price, event_date, event_name, seat_number, gate_entry, is_available, includes_meals, hotel_name):
        # Set ticket_type to "Weekend"
        super().__init__(ticket_id, "Weekend", price, event_date, event_name, seat_number, gate_entry, is_available)
        self.__includes_meals = includes_meals
        self.__hotel_name = hotel_name

    # Getters and setters for extra attributes
    def getIncludesMeals(self):
        return self.__includes_meals

    def setIncludesMeals(self, includes_meals):
        self.__includes_meals = includes_meals

    def getHotelName(self):
        return self.__hotel_name

    def setHotelName(self, hotel_name):
        self.__hotel_name = hotel_name

    def displayWeekendPackage(self):
        return f"Weekend Package - Hotel: {self.__hotel_name} | Meals Included: {self.__includes_meals}"


# GroupTicket Class (Inherits Ticket)

class GroupTicket(Ticket):
    def __init__(self, ticket_id, price, event_date, event_name, seat_numbers, gate_entry, is_available, group_size, discount_rate):
        # Set ticket_type to "Group"
        super().__init__(ticket_id, "Group", price, event_date, event_name, seat_numbers, gate_entry, is_available)
        self.__group_size = group_size
        self.__discount_rate = discount_rate
        self.__seat_numbers = seat_numbers  # List of seats

    # Getters and setters
    def getGroupSize(self):
        return self.__group_size

    def setGroupSize(self, group_size):
        self.__group_size = group_size

    def getSeatNumbers(self):
        return self.__seat_numbers

    def setSeatNumbers(self, seat_numbers):
        self.__seat_numbers = seat_numbers

    def getDiscountRate(self):
        return self.__discount_rate

    def setDiscountRate(self, discount_rate):
        self.__discount_rate = discount_rate

    def displayGroupTicket(self):
        return f"Group Ticket - Size: {self.__group_size} | Discount: {self.__discount_rate * 100}%"


# Booking Class
class Booking:
    def __init__(self, booking_date, is_confirmed):
        # Private attributes for booking details
        self.__booking_date = booking_date
        self.__is_confirmed = is_confirmed

    # Getter and setter for booking date
    def getBookingDate(self):
        return self.__booking_date

    def setBookingDate(self, booking_date):
        self.__booking_date = booking_date

    # Getter and setter for confirmed status
    def isConfirmed(self):
        return self.__is_confirmed

    def setConfirmed(self, confirmed):
        self.__is_confirmed = confirmed



# BookingHistory Class

class BookingHistory:
    def __init__(self, booking_id, user_id, ticket_id, booking_date):
        # Stores a record of one booking: who booked what and when
        self.__booking_id = booking_id
        self.__user_id = user_id
        self.__ticket_id = ticket_id
        self.__booking_date = booking_date

    # Getter and setter for booking ID
    def getBookingID(self):
        return self.__booking_id

    def setBookingID(self, booking_id):
        self.__booking_id = booking_id

    # Getter and setter for user ID
    def getUserID(self):
        return self.__user_id

    def setUserID(self, user_id):
        self.__user_id = user_id

    # Getter and setter for ticket ID
    def getTicketID(self):
        return self.__ticket_id

    def setTicketID(self, ticket_id):
        self.__ticket_id = ticket_id

    # Getter and setter for booking date
    def getBookingDate(self):
        return self.__booking_date

    def setBookingDate(self, booking_date):
        self.__booking_date = booking_date


# Payment Class (Base)

class Payment:
    def __init__(self, payment_id, amount, method, payment_date):
        # Common payment details shared by all payment types
        self.__payment_id = payment_id
        self.__amount = amount
        self.__method = method
        self.__payment_date = payment_date

    # Getter and setter for payment ID
    def getPaymentID(self):
        return self.__payment_id

    def setPaymentID(self, payment_id):
        self.__payment_id = payment_id

    # Getter and setter for amount
    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount

    # Getter and setter for payment method
    def getMethod(self):
        return self.__method

    def setMethod(self, method):
        self.__method = method

    # Getter and setter for payment date
    def getPaymentDate(self):
        return self.__payment_date

    def setPaymentDate(self, payment_date):
        self.__payment_date = payment_date

    def displayPayment(self):
        return f"Payment ID: {self.__payment_id} | Method: {self.__method} | Amount: {self.__amount}"



# CreditCardPayment Class (Inherits Payment)

class CreditCardPayment(Payment):
    def __init__(self, payment_id, amount, payment_date, card_number, card_holder_name, expiry_date):
        # Call parent constructor with method set to "Credit Card"
        super().__init__(payment_id, amount, "Credit Card", payment_date)
        self.__card_number = card_number
        self.__card_holder_name = card_holder_name
        self.__expiry_date = expiry_date

    # Getters and setters for credit card details
    def getCardNumber(self):
        return self.__card_number

    def setCardNumber(self, card_number):
        self.__card_number = card_number

    def getCardHolderName(self):
        return self.__card_holder_name

    def setCardHolderName(self, name):
        self.__card_holder_name = name

    def getExpiryDate(self):
        return self.__expiry_date

    def setExpiryDate(self, expiry_date):
        self.__expiry_date = expiry_date

    def displayCreditCardPayment(self):
        return f"Card: {self.__card_number} | Holder: {self.__card_holder_name} | Expiry: {self.__expiry_date}"


# CashPayment Class (Inherits Payment)

class CashPayment(Payment):
    def __init__(self, payment_id, amount, payment_date, cash_amount, change):
        # Call parent constructor with method set to "Cash"
        super().__init__(payment_id, amount, "Cash", payment_date)
        self.__cash_amount = cash_amount
        self.__change = change

    # Getters and setters for cash-specific info
    def getCashAmount(self):
        return self.__cash_amount

    def setCashAmount(self, cash_amount):
        self.__cash_amount = cash_amount

    def getChange(self):
        return self.__change

    def setChange(self, change):
        self.__change = change
