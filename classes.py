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
