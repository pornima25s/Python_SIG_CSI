# 'f' in Print Statement

a = 4
b = 5
result = a+b

# print("The result is result for the addition")
# print("The result is", result, "for the addition")
# print(f"The result is {result} for the addition")

# FUNCTIONS

def add_1(a, b):
    c = a+b
    print(c)

def add_2(a, b):
    c = a+b
    return c

# add_1(4, 5)
# result = add_2(4, 5)
# print(result)

# print(add_1(4, 5))
# print(add_2(4, 5)) 


# BUILT IN FUNCTIONS

numbers = [3, 2, 1, 5, 4]
# print("Length:", len(numbers))
# print("Sum:", sum(numbers))
# print("Maximum:", max(numbers))
# print("Minimum:", min(numbers))
# print("Sorted:", sorted(numbers)) 

# DEFAULT PARAMETERS

def greet(name="Adi"):
    print(f"Hello, {name}")

greet()
greet("Harry") 