name = "Ada Lovelace"

# Convert string to upper case
print(name.upper())

# Convert string to lowercase
print(name.lower())

title = "trial of tetsing"

# Convert string to Title
print(title.title())

first_name = "ada"
last_name = "lovelace"
# Insert a variable into a string
full_name = f"{first_name} {last_name}" # The stringh printed is inside the ""
print(full_name.title())

# Add a tab
print("\t")

# Add a newline
print("\n")

# String whitespace from end of string
favourite_langague = " python "
print(favourite_langague.rstrip())
print(favourite_langague.lstrip())
favourite_langague = " python "
print(favourite_langague.strip())

# Removing prefix (ex. websites)
url = 'https://nostarch.com'
print(url.removeprefix("https://"))

# Exponents
print(2**4)

# Long numbers
age = 14_000_000_000

# Multiple assignment
x, y, z = 1, 2, 3

# Lists
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
motorcycles.insert(2, 'harley') # Moves the rest to the right, inserts at index
del motorcycles[2] # Removes item from a position in list
popped_motoorcycle = motorcycles.pop() # Removes the last item in a list
# Can also use pop with index
popped_motoorcycle = motorcycles.pop(1)

motorcycles.append("ducati")
# Remove item by value
motorcycles.remove('ducati')

# Organizing Lists
cars = ['bmw', 'audi', 'toyota', 'subaru']
# Sort list alphabetically
cars.sort()
# Sort reverse alphabetically
cars.sort(reverse=True)
# Sorted function displays list in sorted order but doesn't permanetly change order
print(sorted(cars))
# Sort list in reverse
cars.reverse()

# Finding length of list
len(cars)

# Looping with lists
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!\n")

# Generating a series of numbers from 1 to n-1
for value in range(1,5): # Thus this prints numbers 1, 2, 3, 4
    print(value)

for value in range(5):  # Prints numbers 0, 1, 2, 3, 4
    print(value)

# Generating a series of numbers from range()
numbers = list(range(1,6))

# Third argument to range is a step size functon
even_numbers = list(range(2, 11, 2))

# List comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Prints the values from indices 0 to 3
print(players[0:3])
# Prints the values from the start to 3
print(players[:3])
# Prints the values from 2 onwards
print(players[2:])
# Negative index returns an element from a certain distance form the end
print(players[-1])
# Start at the first and end at the last
print(players[:])
# Prints the last three elements of the list
print(players[-3:])

# Defining a tuple
dimensions = (200, 50)
# Can't alter a tuple, nmeed to redefine
dimensions = (400, 100)