
a = 10
b = 5
print(a + b)  # Addition
print(a > b and b < 10)  # Logical AND



#----------------------------------------------------------------------------------------------------


#Addition (+)
print(2 + 3)  # Output: 5



#Subtraction (-)
print(3 - 2)  # Output: 1



#Division (/)
print(35 / 5)  # Output: 7.0 (float)



#Multiplication (*)
print(7 * 4)  # Output: 28



#-------------------------------------------------------------------------------------------------


# Taking two inputs from the user

x = float(input("Enter the first number: "))  # First number (float for flexibility)
y = float(input("Enter the second number: ")) # Second number (float for flexibility)

# Arithmetic Operations
print("\nArithmetic Operations:")
print(f"Addition: {x} + {y} = {x + y}")         # Addition
print(f"Subtraction: {x} - {y} = {x - y}")      # Subtraction
print(f"Multiplication: {x} * {y} = {x * y}")   # Multiplication
print(f"Division: {x} / {y} = {x / y}")         # Division
print(f"Modulus: {x} % {y} = {x % y}")          # Remainder of division

# Logical Operations
print("\nLogical Operations:")
print(f"Is {x} greater than {y}? {x > y}")      # Logical comparison (greater than)
print(f"Is {x} less than {y}? {x < y}")         # Logical comparison (less than)
print(f"Is {x} equal to {y}? {x == y}")         # Logical comparison (equal to)
print(f"Is {x} not equal to {y}? {x != y}")     # Logical comparison (not equal)

# Additional logical operations combining conditions
print("\nCombined Logical Conditions:")
print(f"Is {x} greater than 0 AND {y} greater than 0? {x > 0 and y > 0}")  # AND condition
print(f"Is {x} greater than 0 OR {y} greater than 0? {x > 0 or y > 0}")    # OR condition
print(f"Is NOT {x} greater than {y}? {not (x > y)}")                      # NOT condition
