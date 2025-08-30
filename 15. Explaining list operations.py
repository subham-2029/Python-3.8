"""
List Operations in Python - Detailed Explanation

A list in Python is a mutable, ordered collection of items. Lists can store elements of different types.

Creating a List:
"""
my_list = [1, 2, 3, 'apple', 4.5]
print("Initial list:", my_list)

# Accessing Elements
print("First element:", my_list[0])      # Indexing starts at 0
print("Last element:", my_list[-1])      # Negative index for last element

# Slicing
print("Slice [1:4]:", my_list[1:4])      # Elements from index 1 to 3

# Adding Elements
my_list.append('banana')                 # Adds to end
print("After append:", my_list)

my_list.insert(2, 'orange')              # Inserts at index 2
print("After insert:", my_list)

my_list.extend([6, 7])                   # Adds multiple elements
print("After extend:", my_list)

# Removing Elements
my_list.remove('apple')                  # Removes first occurrence
print("After remove:", my_list)

removed = my_list.pop()                  # Removes and returns last element
print("After pop:", my_list, "| Popped:", removed)

del my_list[1]                           # Deletes element at index 1
print("After del:", my_list)

# Searching
print("'banana' in list?", 'banana' in my_list)
print("Index of 'orange':", my_list.index('orange'))

# Counting
print("Count of 6:", my_list.count(6))

# Sorting
numbers = [3, 1, 4, 2]
numbers.sort()                           # Sorts in place
print("Sorted numbers:", numbers)

# Reversing
numbers.reverse()
print("Reversed numbers:", numbers)

# Copying
copy_list = my_list.copy()
print("Copied list:", copy_list)

# Clearing
my_list.clear()
print("Cleared list:", my_list)

"""
Summary of List Methods:
- append(x): Add x to end
- insert(i, x): Insert x at index i
- extend(iterable): Add all items from iterable
- remove(x): Remove first occurrence of x
- pop([i]): Remove and return item at index i (default last)
- del list[i]: Delete item at index i
- index(x): Return index of first occurrence of x
- count(x): Count occurrences of x
- sort(): Sort list
- reverse(): Reverse list
- copy(): Shallow copy
- clear(): Remove all items
"""
