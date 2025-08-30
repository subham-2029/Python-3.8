# Python Program: Demonstrating Set Methods and Functions

# Sets are unordered collections of unique elements.
# Let's create a set and explore its methods and functions.

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# 1. add(element): Adds an element to the set.
my_set.add(6)
print("After add(6):", my_set)

# 2. update(iterable): Adds multiple elements from an iterable.
my_set.update([7, 8], {9, 10})
print("After update([7, 8], {9, 10}):", my_set)

# 3. remove(element): Removes the specified element. Raises KeyError if not found.
my_set.remove(10)
print("After remove(10):", my_set)

# 4. discard(element): Removes the specified element if present. No error if not found.
my_set.discard(99)  # No error
print("After discard(99):", my_set)

# 5. pop(): Removes and returns an arbitrary element. Raises KeyError if empty.
popped = my_set.pop()
print(f"After pop(): {my_set}, popped element: {popped}")

# 6. clear(): Removes all elements from the set.
temp_set = my_set.copy()
temp_set.clear()
print("After clear():", temp_set)

# 7. copy(): Returns a shallow copy of the set.
copy_set = my_set.copy()
print("Copy of set:", copy_set)

# Set Operations

# 8. union(*others): Returns a new set with elements from the set and all others.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("set_a.union(set_b):", set_a.union(set_b))

# 9. intersection(*others): Returns a new set with elements common to all sets.
print("set_a.intersection(set_b):", set_a.intersection(set_b))

# 10. difference(*others): Returns a new set with elements in the set but not in others.
print("set_a.difference(set_b):", set_a.difference(set_b))

# 11. symmetric_difference(other): Returns a new set with elements in either set, but not both.
print("set_a.symmetric_difference(set_b):", set_a.symmetric_difference(set_b))

# In-place Operations

# 12. update(*others): Updates the set with the union of itself and others.
set_c = {1, 2}
set_c.update({2, 3})
print("After update({2, 3}):", set_c)

# 13. intersection_update(*others): Updates the set with the intersection.
set_d = {1, 2, 3}
set_d.intersection_update({2, 3, 4})
print("After intersection_update({2, 3, 4}):", set_d)

# 14. difference_update(*others): Updates the set with the difference.
set_e = {1, 2, 3, 4}
set_e.difference_update({2, 3})
print("After difference_update({2, 3}):", set_e)

# 15. symmetric_difference_update(other): Updates the set with the symmetric difference.
set_f = {1, 2, 3}
set_f.symmetric_difference_update({2, 3, 4})
print("After symmetric_difference_update({2, 3, 4}):", set_f)

# Set Relations

# 16. issubset(other): Checks if set is subset of other.
print("{1, 2}.issubset({1, 2, 3}):", {1, 2}.issubset({1, 2, 3}))

# 17. issuperset(other): Checks if set is superset of other.
print("{1, 2, 3}.issuperset({1, 2}):", {1, 2, 3}.issuperset({1, 2}))

# 18. isdisjoint(other): Checks if sets have no elements in common.
print("{1, 2}.isdisjoint({3, 4}):", {1, 2}.isdisjoint({3, 4}))

# Built-in Functions

# len(set): Returns the number of elements.
print("len(my_set):", len(my_set))

# min(set), max(set): Returns the smallest/largest element.
print("min(my_set):", min(my_set))
print("max(my_set):", max(my_set))

# sum(set): Returns the sum of elements.
print("sum(my_set):", sum(my_set))

# Membership test: in, not in
print("2 in my_set:", 2 in my_set)
print("99 not in my_set:", 99 not in my_set)

# Iterating over a set
print("Iterating over my_set:")
for item in my_set:
    print(item)

# Sets are mutable and unordered, and do not allow duplicate elements.
# All above methods and functions help in manipulating and querying sets in Python.