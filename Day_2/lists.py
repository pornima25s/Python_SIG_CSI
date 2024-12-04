# CREATING LISTS

numbers = [5, 2, 9, 1, 7]
print(numbers)
days = ["Monday", "Tuesday", "Sunday"]

# BASIC OPERATIONS ON THEM


numbers.append(3)
print("After Append:", numbers)

numbers.insert(1, 10)
print("After Insert:", numbers)

numbers.remove(7)
print("After Remove:", numbers) 

# numbers.append(3)
# print(numbers)
# numbers.remove(3)
# print(numbers)
# # ACCESSING THE LIST

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# # Slicing
print("First Three Elements:", numbers[:3])
print("Last Two Elements:", numbers[-2:])
# print(numbers[2:4])

# # METHODS ON LIST

# Sorting
numbers.sort()
print("Sorted List:", numbers)

# Reversing
numbers.reverse()
print("Reversed List:", numbers)

# Counting occurrences
print("Count of 2:", numbers.count(2))

# Finding index
print("Index of 9:", numbers.index(9))


# # NESTED LISTS

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
# matrix[1][2]
print("Element at [1][2]:", matrix[1][2]) 


