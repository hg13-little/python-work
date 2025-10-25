#8.1

def display_message():
    print("I am learning about functions in this chapter!") 

    display_message()

#8.2
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.") 

    favorite_book("to kill a mockingbird")

#8.3
def make_shirt(size, message):
    print(f"The shirt size is {size} and it has the message: '{message}' printed on it.")

    make_shirt("L", "I love tacos!")
    make_shirt(size="M", message="Python is Fun!")


#8.4
def make_shirt(size="large", message="I love Python"):
    print(f"The shirt size is {size} and it will have the message: '{message}'.")

make_shirt()

make_shirt(size="medium")


make_shirt(size="small", message="Code all day!")

#8.5
def describe_city(city, country="USA"):
    print(f"{city} is in {country}.")       

describe_city("New York")
describe_city("Los Angeles")
describe_city("Philadelphia")

#8.6
def city_country(city, country):
    return f'"{city}, {country}"'      

city1 = city_country("Santiago", "Chile")
city2 = city_country("Cairo", "Egypt")
city3 = city_country("Helsinki", "Finland")

print(city1)
print(city2)
print(city3)

#8.7
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album


album1 = make_album("Taylor Swift", "Midnights")
album2 = make_album("Bad Bunny", "Un Verano Sin Ti")
album3 = make_album("Adele", "30", songs=12)

print(album1)
print(album2)
print(album3)

#8.8
def make_album(artist, title, songs=None):
    """Return a dictionary describing a music album."""
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

while True:
    print("\nEnter album information (or type 'quit' to stop).")

    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break

    title = input("Album title: ")
    if title.lower() == 'quit':
        break

    songs = input("Number of songs (press Enter to skip): ")
    if songs.lower() == 'quit':
        break

    if songs:
        album_info = make_album(artist, title, int(songs))
    else:
        album_info = make_album(artist, title)

    print("Album created:", album_info)

#8.9
def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

text_messages = ["Hey there!", "How are you?", "Don’t forget our meeting!", "See you soon!"]

show_messages(text_messages)

#8.10
def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
        
messages = ["Hey there!", "How are you?", "Don’t forget our meeting!", "See you soon!"]
sent_messages = []

send_messages(messages, sent_messages)

print("\nOriginal list:", messages)
print("Sent messages:", sent_messages)

#8.11
def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hey there!", "How are you?", "Don’t forget our meeting!", "See you soon!"]
sent_messages = []

send_messages(messages[:], sent_messages)

print("\nOriginal list (should still have messages):", messages)
print("Sent messages:", sent_messages)

#8.12
def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!")

make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("ham", "cheese")
make_sandwich("peanut butter", "jelly", "banana", "honey")


#8.13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

my_profile = build_profile(
    "Hector",
    "Gonzalez",
    age=20,
    major="Computer Science",
    hobby="playing football"
)

print(my_profile)

#8.14

def make_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)