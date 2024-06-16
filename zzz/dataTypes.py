# Methods that modify the original list:
#
# append(element):
# Adds an element to the end of the list. The original list is modified.

# extend(iterable):
# Extends the list by appending elements from another iterable. The original list is modified.

# insert(index, element):
# Inserts an element at a specific index. The original list is modified.

# remove(element):
# Removes the first occurrence of a specified element. The original list is modified.

# pop(index=-1):
# Removes and returns the element at a specified index (default: last element). The original list is modified.

# sort(key=None, reverse=False):
# Sorts the list in place. The original list is modified.

# reverse():
# Reverses the elements of the list in place. The original list is modified.


# 1. String to List:
fruits_string = "apple,banana,cherry"
fruits_list = fruits_string.split(",")
print(f"String: {fruits_string}\nList: {fruits_list}")

#String: apple,banana,cherry
#List: ['apple', 'banana', 'cherry']


# 2. List to Tuple:
colors_list = ["red", "green", "blue"]
colors_tuple = tuple(colors_list)
print(f"List: {colors_list}\nTuple: {colors_tuple}")

#List: ['red', 'green', 'blue']
#Tuple: ('red', 'green', 'blue')

# 3. Tuple to Set:
numbers_tuple = (1, 2, 2, 3, 4)
numbers_set = set(numbers_tuple)
print(f"Tuple: {numbers_tuple}\nSet: {numbers_set}")

#Tuple: (1, 2, 2, 3, 4)
#Set: {1, 2, 3, 4}

# 4. Set to List:
chars_set = {'a', 'b', 'c'}
chars_list = list(chars_set)
print(f"Set: {chars_set}\nList: {chars_list}")

#Set: {'a', 'b', 'c'}
#List: ['c', 'a', 'b']

# 5. List to Set:

fruits_list = ["apple", "banana", "cherry", "apple"]  # List with a duplicate
fruits_set = set(fruits_list)
print(f"List: {fruits_list}\nSet: {fruits_set}")
