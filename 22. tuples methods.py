# Tuple Methods Explained in Python

# Tuples are immutable sequences in Python.
# They have only two built-in methods: count() and index().
# Let's explore them with examples and explanations.

# 1. count(x)
# Returns the number of times x appears in the tuple.

my_tuple = (1, 2, 3, 2, 4, 2, 5)
count_2 = my_tuple.count(2)
print(f"count(2): {count_2}")  # Output: 3

# Explanation:
# The count() method scans the tuple and counts how many times the value '2' occurs.

# 2. index(x[, start[, end]])
# Returns the first index at which x is found in the tuple.
# Optional start and end arguments can limit the search.

index_3 = my_tuple.index(3)
print(f"index(3): {index_3}")  # Output: 2

# Explanation:
# The index() method returns the position of the first occurrence of '3' in the tuple.

# Using start and end arguments:
index_2_after_2 = my_tuple.index(2, 2)  # Start searching from index 2
print(f"index(2, 2): {index_2_after_2}")  # Output: 3

# If the value is not found, index() raises a ValueError:
try:
    my_tuple.index(10)
except ValueError as e:
    print(f"index(10): {e}")  # Output: tuple.index(x): x not in tuple

# Summary:
# Tuples only have two methods:
# - count(x): Counts occurrences of x.
# - index(x[, start[, end]]): Finds the index of x, with optional search bounds.

# For more tuple operations, you can use built-in functions like len(), min(), max(), etc.,
# but these are not tuple methods as there are separate functions for tuples.