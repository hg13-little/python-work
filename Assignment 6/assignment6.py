6.1
person = {
    'first_name': 'hector',
    'last_name': 'gonzalez',
    'age': 18,
    'city': 'New York'
}

print("First Name:", person['first_name'])
print("Last Name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])

6.2 
favorite_numbers = {
    'Alice': 7,
    'Haidy': 42,
    'Hilary': 3,
    'Hector': 13,
    'Ethan': 27
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

6.3
glossary = {
    'variable': 'A named location used to store data in memory.',
    'function': 'A block of code that performs a specific task when called.',
    'loop': 'A control structure used to repeat a block of code multiple times.',
    'list': 'An ordered collection of items that can be changed.',
    'dictionary': 'A collection of key-value pairs where each key is unique.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")

6.4
glossary = {
    'variable': 'A named location used to store data in memory.',
    'function': 'A block of code that performs a specific task when called.',
    'loop': 'A control structure used to repeat a block of code multiple times.',
    'list': 'An ordered collection of items that can be changed.',
    'dictionary': 'A collection of key-value pairs where each key is unique.',
    'tuple': 'An ordered, immutable collection of items.',
    'if statement': 'Used to make decisions in code based on conditions.',
    'boolean': 'A data type with only two values: True or False.',
    'comment': 'Text in the code that is not executed; used for documentation.',
    'indentation': 'Whitespace used at the beginning of lines to define blocks of code.'
}

for term, definition in glossary.items():
    print(f"{term.title()}:\n  {definition}\n")

6.5 
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

for river, country in rivers.items():
    print(f"The{river.title()} runs through {country.title()}.")
print("\nNames of the rivers:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nNames of the countries:")
for country in rivers.values():
    print(f"- {country.title()}")

6.6

favorite_languages = {
    'alice': 'python',
    'john': 'java',
    'derek': 'c++',
    'densel': 'javascript'
}

people_to_poll = ['alice', 'john', 'derek', 'densel', 'charlie']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, we invite you to take our favorite languages poll!")
6.7
person1 = {
    'first_name': 'hector',
    'last_name': 'gonzalez',
    'age': 18,
    'city': 'New York'
}

person2 = {
    'first_name': 'Bob',
    'last_name': 'Smith',
    'age': 35,
    'city': 'Los Angeles'
}

person3 = {
    'first_name': 'Charlie',
    'last_name': 'Davis',
    'age': 22,
    'city': 'Chicago'
}
people = [person1, person2, person3]

for person in people:
    print(f"\nInformation about {person['first_name']} {person['last_name']}:")
    print(f"  First Name: {person['first_name']}")
    print(f"  Last Name: {person['last_name']}")
    print(f"  Age: {person['age']}")
    print(f"  City: {person['city']}")

6.8
pet1 = {
    'animal': 'dog',
     'name': 'Buddy',
    'owner': 'Alice'
}


pet2 = {
    'animal': 'cat',
    'name': 'Willow',
    'owner': 'Bob'
}

pet3 = {
    'animal': 'parrot',
    'name': 'Peter',
    'owner': 'Charlie'
}

pet4 = {
    'animal': 'rabbit',
    'name': 'Theodore',
    'owner': 'Diana'
}

pet5 = {
    'animal': 'hamster',
    'name': 'Nigel',
    'owner': 'Ethan'
}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print(f"\nPet Name: {pet['name']}")
    print(f"  Animal Type: {pet['animal'].title()}")
    print(f"  Owner: {pet['owner']}")

6.9
favorite_places ={
    'alice': ['paris', 'kyoto', 'new york'],
    'bob':['rome'],
    'cj':['sydney', 'cape town']
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite place(s):")
    for place in places:
        print(f"  - {place.title()}")
    
6.10
favorite_numbers = {
    'alice': [7, 14, 21],
    'haidy': [42],
    'hilary': [3, 9],
    'hector': [12, 24],
    'ethan': [27, 36, 45]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"  - {number}")

6.11
cities = {
    'london': {
        'country': 'United Kingdom',
        'population': '9 million',
        'fact': 'Famous for the historic Tower of London and the Big Ben clock tower.'
    },
    'sydney': {
        'country': 'Australia',
        'population': '5.3 million',
        'fact': 'Known for the iconic Sydney Opera House and Harbour Bridge.'
    },
    'cape town': {
        'country': 'South Africa',
        'population': '4.6 million',
        'fact': 'Famous for Table Mountain and beautiful coastal scenery.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")

6.12
cities = {
    'london': {
        'country': 'United Kingdom',
        'population': '9 million',
        'area': '1,572 km²',
        'timezone': 'GMT',
        'fact': 'Famous for the historic Tower of London and the Big Ben clock tower.'
    },
    'sydney': {
        'country': 'Australia',
        'population': '5.3 million',
        'area': '12,367 km²',
        'timezone': 'AEST',
        'fact': 'Known for the iconic Sydney Opera House and Harbour Bridge.'
    },
    'cape town': {
        'country': 'South Africa',
        'population': '4.6 million',
        'area': '2,461 km²',
        'timezone': 'SAST',
        'fact': 'Famous for Table Mountain and beautiful coastal scenery.'
    },
    'berlin': {
        'country': 'Germany',
        'population': '3.7 million',
        'area': '891.8 km²',
        'timezone': 'CET',
        'fact': 'Known for its art scene and the Berlin Wall history.'
    },
    'rio de janeiro': {
        'country': 'Brazil',
        'population': '6.7 million',
        'area': '1,255 km²',
        'timezone': 'BRT',
        'fact': 'Famous for its Carnival festival and Christ the Redeemer statue.'
    }
}

for city, info in cities.items():
    print(f"\n{'='*40}")
    print(f"City: {city.title()}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Area: {info['area']}")
    print(f"Timezone: {info['timezone']}")
    print(f"Fun Fact: {info['fact']}")
print(f"{'='*40}")