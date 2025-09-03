# Hector 
# Date: 2025-09-03
# this program prints a qoute said by lebron james 
H = "Hector"
print(H)
print(H.upper())
print(H.lower())
print(H.title())

full_name = "Lebron james"
message = f"'You can't be afraid to fail. It's the only way you succeed, by {full_name.title()}'"
print(message)
famous_person = "Hugh Jackman"
message = f"{famous_person} once said, \"Unless you're willing to fail miserably in the pursuit of your dreams, you'll never make it.\""
print(message)

name = "\t\n Goku \n\t"

print("Original with whitespace:")
print(repr(name))

print("\nAfter lstrip():")
print (repr(name.lstrip()))

print("\nAfter strip():")
print(repr(name.strip()))

print("\nAfter rstrip():")
print(repr(name.rstrip()))

filename = "python_notes.txt"
name_without_extension = filename.removesuffix(".txt")
print(name_without_extension)

print(5 + 3)
print(7 + 1)
print(6 + 2)
print(4 + 4)

favorite_number = 13
message = f"my favorite number is {favorite_number}"
print(message)