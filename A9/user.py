class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}\n"
              f"Age: {self.age}\nLocation: {self.location}\nEmail: {self.email}\n")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!\n")
        