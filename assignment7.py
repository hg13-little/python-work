7.1
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")

7.2
people = int(input("How many people are in your dinner group? "))

if people > 4:
    print("You’ll have to wait for a table.")
else:
    print("Your table is ready.")

7.3
number = int(input("Enter a number: "))

if number % 20 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")

7.4
topping = ""

while topping.lower() != 'quit':
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping.lower() != 'quit':
        print(f"I’ll add {topping} to your pizza.")

7.5 
while True:
    age = input("Enter your age (or 'quit' to exit): ")

    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

7.6-1
topping = ""
while topping.lower() != 'quit':
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping.lower() != 'quit':
        print(f"Adding {topping} to your pizza.")

7.6-2
active = True

while active:
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")

7.6-3 
while True:
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")   

7.7
while True:
    print("This loop runs forever!")     







    
    
    
    
    
    
    
    
    
    
    
    
   