7.8
sandwich_orders = ['tuna', 'ham', 'turkey', 'roast beef', 'chicken salad']
finished_sandwiches = []

while sandwich_orders:
 current_sandwich = sandwich_orders.pop(0)

print(f"I made your {current_sandwich} sandwich.")
finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
   print(f"- {sandwich.title()} sandwich")


7.9
sandwich_orders = [
    'tuna', 'pastrami', 'ham', 'pastrami', 
    'turkey', 'pastrami', 'chicken salad'
]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)


print("\nAll sandwiches have been made (no pastrami):")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")



7.10
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

    responses[name] = vacation

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Dream Vacation Results ---")
for name, vacation in responses.items():
    print(f"{name.title()} would like to visit {vacation.title()}.")