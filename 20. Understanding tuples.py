# Tuples in Python - Detailed Explanation

# What is a tuple?
# A tuple is an immutable, ordered collection of items. Tuples are similar to lists, but unlike lists, tuples cannot be changed after creation.

# Creating tuples
empty_tuple = ()
single_element_tuple = (42,)  # Note the comma!
multi_element_tuple = (1, 2, 3, 'a', 'b')

print("Empty tuple:", empty_tuple)
print("Single element tuple:", single_element_tuple)
print("Multiple element tuple:", multi_element_tuple)

# Accessing elements
print("First element:", multi_element_tuple[0])
print("Last element:", multi_element_tuple[-1])

# Slicing tuples
print("Slice [1:4]:", multi_element_tuple[1:4])

# Tuple unpacking
a, b, c, d, e = multi_element_tuple
print("Unpacked values:", a, b, c, d, e)

# Immutability
try:
    multi_element_tuple[0] = 99  # This will raise an error
except TypeError as e:
    print("Tuples are immutable:", e)

# Nested tuples
nested_tuple = ((1, 2), (3, 4))
print("Nested tuple:", nested_tuple)
print("Access nested element:", nested_tuple[1][0])

# Tuple methods
# Tuples have only two built-in methods: count() and index()
sample_tuple = (1, 2, 2, 3, 2)
print("Count of 2:", sample_tuple.count(2))
print("Index of 3:", sample_tuple.index(3))

# When to use tuples?
# - When you need an immutable sequence of items
# - For returning multiple values from functions
# - As keys in dictionaries (if all elements are immutable)

# Example: Returning multiple values from a function
def min_max(numbers):
    return (min(numbers), max(numbers))

result = min_max([4, 7, 1, 9])
print("Min and Max:", result)

# Example: Using tuples as dictionary keys
locations = { (35.6895, 139.6917): "Tokyo", (51.5074, -0.1278): "London" }
print("City at (51.5074, -0.1278):", locations[(51.5074, -0.1278)])

# Summary
# Tuples are immutable, ordered collections. Use them when you need to ensure data cannot be changed.