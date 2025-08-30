"""
Introduction to Lists in Python
-------------------------------

A list is a built-in data structure in Python that allows you to store multiple items in a single variable.
Lists are ordered, mutable (changeable), and can contain elements of different types.

Creating a List
---------------
You can create a list by placing comma-separated values inside square brackets [].

Examples:
"""

# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A mixed list
mixed = [1, "hello", 3.14, True]

"""
Accessing Elements
------------------
List elements are accessed using their index (position), starting from 0.
"""

print(numbers[0])      # Output: 1
print(fruits[2])       # Output: cherry

"""
Negative indices count from the end:
"""

print(fruits[-1])      # Output: cherry

"""
Modifying Lists
---------------
Lists are mutable, so you can change their contents.
"""

fruits[1] = "orange"
print(fruits)          # Output: ['apple', 'orange', 'cherry']

"""
Adding Elements
---------------
Use append() to add an item to the end of the list.
Use insert() to add an item at a specific position.
"""

fruits.append("grape")
print(fruits)          # Output: ['apple', 'orange', 'cherry', 'grape']

fruits.insert(1, "kiwi")
print(fruits)          # Output: ['apple', 'kiwi', 'orange', 'cherry', 'grape']

"""
Removing Elements
-----------------
Use remove() to delete a specific value.
Use pop() to remove an item at a specific index (default is last item).
"""

fruits.remove("orange")
print(fruits)          # Output: ['apple', 'kiwi', 'cherry', 'grape']

fruits.pop(2)
print(fruits)          # Output: ['apple', 'kiwi', 'grape']

"""
List Length
-----------
Use len() to get the number of items in a list.
"""

print(len(fruits))     # Output: 3

"""
Iterating Through a List
------------------------
You can loop through a list using a for loop.
"""

for fruit in fruits:
    print(fruit)

"""
List Slicing
------------
You can get a part of a list using slicing.
"""

print(numbers[1:4])    # Output: [2, 3, 4]
print(numbers[:3])     # Output: [1, 2, 3]
print(numbers[::2])    # Output: [1, 3, 5]

"""
Other Useful List Methods
-------------------------
- sort(): Sorts the list.
- reverse(): Reverses the list.
- count(): Counts occurrences of a value.
- index(): Finds the index of a value.
"""

numbers.sort()
print(numbers)         # Output: [1, 2, 3, 4, 5]

numbers.reverse()
print(numbers)         # Output: [5, 4, 3, 2, 1]

print(fruits.count("apple"))  # Output: 1
print(fruits.index("kiwi"))   # Output: 1

"""
Summary
-------
Lists are versatile and widely used in Python for storing and manipulating collections of data.
Practice creating, accessing, and modifying lists to become comfortable with this essential data structure.
"""