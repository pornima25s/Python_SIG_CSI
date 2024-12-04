# colors = ("red", "green", "blue")
# print("Tuple:", colors)

# # Accessing elements
# print("First Color:", colors[0])
# print("Last Color:", colors[-1])

# 1. Write a function that takes a number as input and returns its factorial.
# 2. Replace the second element in a list of cities with a new city.

# def factorial(n):
#     result = 1  
#     for i in range(1, n+1):
#         result *= i
#     return result

# result = factorial(7)
# print(result)

cities = ["Pune", "Mumbai", "Nashik", "Nagpur"]
print(cities)
cities[2] = "Aurangabad"
print(cities)

cities.remove("Aurangabad")
cities.insert(2, "Ratnagiri")
print(cities)

# Create a function that prints the first n Fibonacci Numbers where 'n' will be the parameter