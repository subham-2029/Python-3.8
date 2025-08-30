"""
Python List Manipulations - Detailed Explanation

Lists are mutable sequences in Python, used to store collections of items.
Below are common list manipulations with examples and explanations.
"""

# 1. Creating a List
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# 2. Accessing Elements
print("First element:", my_list[0])      # Indexing starts at 0
print("Last element:", my_list[-1])      # Negative indexing

# 3. Slicing
print("Elements from index 1 to 3:", my_list[1:4])  # Slices from index 1 up to 3

# 4. Adding Elements
my_list.append(6)        # Adds 6 to the end
print("After append:", my_list)

my_list.insert(2, 99)    # Inserts 99 at index 2
print("After insert:", my_list)

my_list.extend([7, 8])   # Adds multiple elements at the end
print("After extend:", my_list)

# 5. Removing Elements
my_list.remove(99)       # Removes first occurrence of 99
print("After remove:", my_list)

removed = my_list.pop()  # Removes and returns last element
print("After pop:", my_list, "| Popped:", removed)

removed_at_index = my_list.pop(1)  # Removes and returns element at index 1
print("After pop at index 1:", my_list, "| Popped:", removed_at_index)

del my_list[0]           # Deletes element at index 0
print("After del:", my_list)

# 6. Updating Elements
my_list[0] = 42          # Changes value at index 0
print("After update:", my_list)

# 7. Searching
print("Index of 42:", my_list.index(42))  # Finds index of first occurrence
print("Count of 4:", my_list.count(4))    # Counts occurrences of 4

# 8. Sorting and Reversing
my_list.sort()           # Sorts list in ascending order
print("After sort:", my_list)

my_list.reverse()        # Reverses the list
print("After reverse:", my_list)

# 9. Copying a List
copy_list = my_list.copy()
print("Copied list:", copy_list)

# 10. Clearing a List
my_list.clear()
print("After clear:", my_list)

# 11. List Comprehensions
squared = [x**2 for x in range(5)]
print("List comprehension (squared):", squared)

# 12. Nested Lists
nested = [[1, 2], [3, 4]]
print("Nested list:", nested)
print("Access nested element:", nested[1][0])  # Access 3

# 13. Membership Test
print("Is 4 in squared?", 4 in squared)

# 14. Length of List
print("Length of squared:", len(squared))

# 15. Looping Through a List
for item in squared:
    print("Item:", item)

# Summary:
# - Lists are mutable and versatile.
# - You can add, remove, update, and search elements.
# - Slicing, comprehensions, and nested lists are powerful features.
# - Use built-in methods for efficient manipulations.