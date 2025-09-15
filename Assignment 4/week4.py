menu = ("french fries", "burgers", "tacos", "salad", "Sandwiches","tacos")

print("original menu:")
for food in menu:
    print(f"- {food}")
try:
    menu[0] = "soup"
except TypeError as e:
    print("\nError: Cannot modify a tuple. Tuples are immutable")
    print(f"python says: {e}") 
menu = ("french fries", "Burgers", "Tacos", "sushi", "nachos", ) 
print("\Revised Menu:")
for food in menu:
    print(f"- {food}")