# Implicit conversion from int to float
num_int = 5
num_float = num_int + 2.5
print(num_float)  # Output: 7.5
print(type(num_float))  # Output: <class 'float'>




value = 123
string_value = str(value)
print(string_value)  # Output: "123"
print(type(string_value))  # Output: <class 'str'>



value = "42"
int_value = int(value)
print(int_value)  # Output: 42
print(type(int_value))  # Output: <class 'int'>





#ord(): Converts a character to its Unicode integer value.

print(ord('A'))  # Output: 65


#hex(): Converts an integer to a hexadecimal string.

print(hex(255))  # Output: '0xff'#












# Type Conversion (Casting) Examples

# Integer to Float
int_value = 10
float_value = float(int_value)  # Convert int to float
print(f"Integer to Float: {int_value} -> {float_value}")

# Float to Integer
float_value = 12.56
int_value = int(float_value)  # Convert float to int (truncates the decimal part)
print(f"Float to Integer: {float_value} -> {int_value}")

# Integer to String
int_value = 42
str_value = str(int_value)  # Convert int to string
print(f"Integer to String: {int_value} -> '{str_value}'")

# String to Integer
str_value = "123"
int_value = int(str_value)  # Convert string to int (only works for numeric strings)
print(f"String to Integer: '{str_value}' -> {int_value}")

# String to Float
str_value = "45.67"
float_value = float(str_value)  # Convert string to float
print(f"String to Float: '{str_value}' -> {float_value}")

# Float to String
float_value = 78.9
str_value = str(float_value)  # Convert float to string
print(f"Float to String: {float_value} -> '{str_value}'")

# String to Boolean
str_value = "True"
bool_value = bool(str_value)  # Convert string to boolean (non-empty string becomes True)
print(f"String to Boolean: '{str_value}' -> {bool_value}")

# Integer to Boolean
int_value = 0
bool_value = bool(int_value)  # Convert int to boolean (0 is False, non-zero is True)
print(f"Integer to Boolean: {int_value} -> {bool_value}")

# Boolean to Integer
bool_value = True
int_value = int(bool_value)  # Convert boolean to integer (True is 1, False is 0)
print(f"Boolean to Integer: {bool_value} -> {int_value}")

# List to String (via Join)
list_value = [1, 2, 3]
str_value = ",".join(map(str, list_value))  # Convert each list element to string and join with commas
print(f"List to String: {list_value} -> '{str_value}'")

# String to List
str_value = "apple,banana,cherry"
list_value = str_value.split(",")  # Split string into a list based on commas
print(f"String to List: '{str_value}' -> {list_value}")

# List to Tuple
list_value = [1, 2, 3]
tuple_value = tuple(list_value)  # Convert list to tuple
print(f"List to Tuple: {list_value} -> {tuple_value}")

# Tuple to List
tuple_value = (4, 5, 6)
list_value = list(tuple_value)  # Convert tuple to list
print(f"Tuple to List: {tuple_value} -> {list_value}")

# Set to List
set_value = {7, 8, 9}
list_value = list(set_value)  # Convert set to list
print(f"Set to List: {set_value} -> {list_value}")

# List to Set
list_value = [1, 2, 2, 3]
set_value = set(list_value)  # Convert list to set (removes duplicates)
print(f"List to Set: {list_value} -> {set_value}")

# Dict Keys to List
dict_value = {"a": 1, "b": 2, "c": 3}
keys_list = list(dict_value.keys())  # Convert dict keys to list
print(f"Dict Keys to List: {dict_value} -> {keys_list}")

# Dict Values to List
values_list = list(dict_value.values())  # Convert dict values to list
print(f"Dict Values to List: {dict_value} -> {values_list}")
