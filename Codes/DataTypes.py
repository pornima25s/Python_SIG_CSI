
# Numeric Types
a = 10                 # int: Integer
b = 3.14               # float: Floating-point number
c = 2 + 3j             # complex: Complex number
print("Numeric Types:")
print(f"int: {a}, float: {b}, complex: {c}\n")

# Sequence Types
d = "Hello, World!"    # str: String
e = [1, 2, 3]          # list: Mutable ordered collection
f = (4, 5, 6)          # tuple: Immutable ordered collection
g = range(1, 5)        # range: Immutable sequence of numbers
print("Sequence Types:")
print(f"str: {d}, list: {e}, tuple: {f}, range: {list(g)}\n")

# Set Types
h = {7, 8, 9}          # set: Mutable collection of unique items
i = frozenset({10, 11, 12})  # frozenset: Immutable version of set
print("Set Types:")
print(f"set: {h}, frozenset: {i}\n")

# Mapping Type
j = {"name": "Alice", "age": 25}  # dict: Key-value pairs
print("Mapping Type:")
print(f"dict: {j}\n")

# Boolean Type
k = True               # bool: True or False
print("Boolean Type:")
print(f"bool: {k}\n")

# None Type
l = None               # NoneType: Represents the absence of a value
print("None Type:")
print(f"NoneType: {l}\n")

# User-Defined Types
# 1. Class and Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

m = Person("Bob", 30)
print("User-Defined Type: Class and Object")
print(m.greet(), "\n")

# 2. Functions as Data (First-Class Functions)
def say_hello():
    return "Hello from a function!"

n = say_hello          # Assign function to a variable
print("User-Defined Type: Functions as Data")
print(n())             # Call the function using the variable



#---------------------------------------------------------------------------