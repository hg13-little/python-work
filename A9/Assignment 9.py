class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Bella Italia", "Italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2
restaurant1 = Restaurant("Sushi World", "Japanese")
restaurant2 = Restaurant("Taco Fiesta", "Mexican")
restaurant3 = Restaurant("Curry House", "Indian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"User Information:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Location: {self.location}\n"
              f"Email: {self.email}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.\n")

user1 = User("Alice", "Johnson", 28, "New York", "alice@example.com")
user2 = User("Carlos", "Ramirez", 35, "Los Angeles", "carlos@example.com")
user3 = User("Maria", "Lopez", 22, "Miami", "maria@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

#9-4 
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers

restaurant = Restaurant("Bella Italia", "Italian")



print(f"Customers served: {restaurant.number_served}")


restaurant.number_served = 25
print(f"Customers served after update: {restaurant.number_served}")

restaurant.set_number_served(40)
print(f"Customers served after set_number_served(): {restaurant.number_served}")


restaurant.increment_number_served(30)
print(f"Customers served after increment: {restaurant.number_served}")

#9-5
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  

    def describe_user(self):
        print(f"User Information:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Location: {self.location}\n"
              f"Email: {self.email}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.\n")

    def increment_login_attempts(self):
        """Increase login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


user = User("Alice", "Johnson", 28, "New York", "alice@example.com")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")

#9-6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "mint"]

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

icecream_stand = IceCreamStand("Frosty Delights")
icecream_stand.describe_restaurant()
icecream_stand.display_flavors()

#9-7
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}\n"
              f"Age: {self.age}\nLocation: {self.location}\nEmail: {self.email}\n")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("Laura", "Smith", 40, "Chicago", "laura@example.com")
admin.describe_user()
admin.show_privileges()

#9-8
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()


admin2 = Admin("David", "Lee", 33, "Seattle", "david@example.com")
admin2.describe_user()
admin2.privileges.show_privileges()


#9-9
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if it isn’t already 65."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already upgraded.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar("Tesla", "Model 3", 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#9-13
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)


# 6-sided
die_6 = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(die_6.roll_die(), end=" ")
print("\n")

# 10-sided
die_10 = Die(10)
print("Rolling a 10-sided die 10 times:")
for _ in range(10):
    print(die_10.roll_die(), end=" ")
print("\n")

# 20-sided
die_20 = Die(20)
print("Rolling a 20-sided die 10 times:")
for _ in range(10):
    print(die_20.roll_die(), end=" ")
print()

#9-14
import random

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 'A', 'B', 'C', 'D', 'E']

winning_combination = random.sample(lottery_items, 4)

print("Any ticket matching these 4 numbers/letters wins a prize!")
print("Winning combination:", winning_combination)

import random

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 'A', 'B', 'C', 'D', 'E']

my_ticket = [3, 'B', 7, 'E']

attempts = 0

while True:
    attempts += 1
    winning_combo = random.sample(lottery_items, 4)
    if set(winning_combo) == set(my_ticket):
        break

print(f"It took {attempts} tries to win the lottery!")