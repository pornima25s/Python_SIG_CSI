# 1. Write a function that takes a number as input and returns its factorial.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5)) 


# 2. Replace the second element in a list of cities with a new city.

cities = ["New York", "London", "Paris"]
cities[1] = "Tokyo"
print(cities)  


# 3. Write a function that prints the first n Fibonacci numbers.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(7) 


