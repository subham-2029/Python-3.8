# Python Program: Brief Explanation of Sets

# Sets are unordered collections of unique elements.
# They are useful for removing duplicates and performing set operations.

# Creating a set
my_set = {1, 2, 3, 4, 4, 2}
print("Set with duplicates removed:", my_set)  # Output: {1, 2, 3, 4}

# Adding elements
my_set.add(5)
print("After adding 5:", my_set)

# Removing elements
my_set.remove(2)
print("After removing 2:", my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union:", set_a | set_b)        # {1, 2, 3, 4, 5}
print("Intersection:", set_a & set_b) # {3}
print("Difference:", set_a - set_b)   # {1, 2}

# Sets do not allow indexing or slicing since they are unordered.