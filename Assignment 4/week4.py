tacos = ['steak', 'vegan', 'chicken']

for taco in tacos:
    print(f"I like {taco} tacos.")

print("\nI enjoy trying different kinds of tacos.")
print("steak has that classic flavor I never get tired of.")
print("vegan is so fresh and simple—perfect comfort food.")
print("chicken brings a smoky twist that I love!")
print("I really love tacos!")

animals = ['dog', 'bird', 'cat']

for animal in animals:
    print(f"A {animal} would make a great pet.")

print("\nAll of these animals are friendly")
print("They are also great companions.")
print("Any of these animals would make a great pet")

for number in range(1,21):
    print(number)
numbers = list(range(1, 1_000_001))
numbers = list(range(1, 1_000_001))

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))

odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)

threes = list(range(3, 31, 3))

for number in threes:
    print(number)

cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)
    print(cube)

cubes = [number ** 3 for number in range(1, 11)]
print(cubes)


pizzas = ['pepperoni', 'margherita', 'bbq chicken', 'hawaiian', 'veggie']

print("The first three items in the list are:")
print(pizzas[:3])

print("Three items from the middle of the list are:")
print(pizzas[1:4])

print("The last three items in the list are:")
print(pizzas[-3:])

pizzas = ['pepperoni', 'margherita', 'bbq chicken']
friend_pizzas = pizzas[:]

pizzas.append('hawaiian')
friend_pizzas.append('mushroom')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = ['ice cream', 'sushi', 'pasta']

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend’s favorite foods are:")
for food in friend_foods:
    print(food)

buffet_foods = ('fried rice', 'noodles', 'grilled chicken', 'salad', 'fruit salad')

print("Original buffet menu:")
for food in buffet_foods:
    print(food)

buffet_foods = ('fried rice', 'noodles', 'sushi', 'dumplings', 'fruit salad')

print("\nRevised buffet menu:")
for food in buffet_foods:
    print(food)