car = 'subaru'
age = 25
name = 'hunter'
temperature = 30
is_raining = False

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs age >= 18? I predict True.")
print(age >= 18)

print("\nIs name.lower() == 'hunter'? I predict True.")
print(name.lower() == 'alice')

print("\nIs temperature > 20? I predict True.")
print(temperature > 20)

print("\nIs is_raining == False? I predict True.")
print(is_raining == False)


print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs name == 'Bob'? I predict False.")
print(name == 'Bob')

print("\nIs temperature < 10? I predict False.")
print(temperature < 10)

print("\nIs is_raining == True? I predict False.")
print(is_raining == True)



fruit = 'pineapple'

print("Is fruit == 'pineapple'? I predict True.")
print(fruit == 'pineapple')

print("\nIs fruit != 'banana'? I predict True.")
print(fruit != 'banana')

print("\nIs fruit == 'banana'? I predict False.")
print(fruit == 'banana')

city = 'new york'

print("\nIs city.lower() == 'new york'? I predict True.")
print(city.lower() == 'new york')

print("\nIs city.lower() == 'NEW YORK'? I predict False.")
print(city.lower() == 'NEW YORK') 

age = 25

print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age != 30? I predict True.")
print(age != 30)

print("\nIs age > 20? I predict True.")
print(age > 20)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 25? I predict True.")
print(age >= 25)

print("\nIs age <= 24? I predict False.")
print(age <= 24)

height = 170
weight = 65

print("\nIs height > 160 and weight < 70? I predict True.")
print(height > 160 and weight < 70)

print("\nIs height > 180 and weight < 70? I predict False.")
print(height > 180 and weight < 70)

print("\nIs height > 180 or weight < 70? I predict True.")
print(height > 180 or weight < 70)

print("\nIs height < 160 or weight > 70? I predict False.")
print(height < 160 or weight > 70)


colors = ['red', 'green', 'blue']

print("\nIs 'green' in colors? I predict True.")
print('green' in colors)

print("\nIs 'yellow' in colors? I predict False.")
print('yellow' in colors)

# === 6. Test whether an item is not in a list ===
print("\nIs 'purple' not in colors? I predict True.")
print('purple' not in colors)

print("\nIs 'red' not in colors? I predict False.")
print('red' not in colors)

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!") 

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points.")

alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

age = 45

if age < 2:
    print("This person is a baby.")
elif age < 4:
    print("This person is a toddler.")
elif age < 13:
    print("This person is a kid.")
elif age < 20:
    print("This person is a teenager.")
elif age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

favorite_fruits = ['mango', 'banana', 'grapes']

if 'banana' in favorite_fruits:
    print("You really like bananas!")

if 'mango' in favorite_fruits:
    print("You really like mangoes!")

if 'apple' in favorite_fruits:
    print("You really like apples!")  

if 'grapes' in favorite_fruits:
    print("You really like grapes!")

if 'orange' in favorite_fruits:
    print("You really like oranges!") 

usernames = ['admin', 'jayden', 'sarah', 'mikey', 'harold']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
    
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

current_users = ['Alice', 'Bob', 'charlie', 'Admin', 'Eve']
new_users = ['Charlie', 'daniel', 'admin', 'frank', 'George']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")