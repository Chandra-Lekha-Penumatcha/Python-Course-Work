class User:
    def __init__( self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def register(self):
        if self.name == "":
            print("Registration failed: name is required")
        elif self.email == "":
            print("Registration failed: email is required")
        elif self.phone == "":
            print("Registration failed: phone  number is required")
        elif self.password == "":
            print("Registration failed: password is required")
        else:
            print("Registration is sucessful")
name = input("name: ")
email = input("email: ")
phone = input("phone: ")
password = input("password: ")

user = User(name, email, phone, password)
user.register()

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self, login_email, login_password):
        if self.email == login_email and self.password == login_password:
            print("Login Successful")
        else:
            print("Invalid Email or Password")


registered_email = input("Registered Email: ")
registered_password = input("Registered Password: ")

login_email = input("Login Email: ")
login_password = input("Login Password: ")

user = User(registered_email, registered_password)
user.login(login_email, login_password)