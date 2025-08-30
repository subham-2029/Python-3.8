# Tuple Operations in Python - Detailed Explanation

# 1. Creating Tuples
empty_tuple = ()
single_element_tuple = (42,)  # Note the comma!
multi_element_tuple = (1, 2, 3, 4)

print("Empty tuple:", empty_tuple)
print("Single element tuple:", single_element_tuple)
print("Multi-element tuple:", multi_element_tuple)

# 2. Accessing Elements
print("First element:", multi_element_tuple[0])
print("Last element:", multi_element_tuple[-1])

# 3. Slicing Tuples
print("Slice [1:3]:", multi_element_tuple[1:3])

# 4. Tuple Immutability
try:
    multi_element_tuple[0] = 99  # This will raise an error
except TypeError as e:
    print("Tuples are immutable:", e)

# 5. Concatenation
tuple_a = (1, 2)
tuple_b = (3, 4)
concatenated = tuple_a + tuple_b
print("Concatenated tuple:", concatenated)

# 6. Repetition
repeated = tuple_a * 3
print("Repeated tuple:", repeated)

# 7. Membership Test
print("Is 2 in tuple_a?", 2 in tuple_a)
print("Is 5 not in tuple_a?", 5 not in tuple_a)

# 8. Iterating Over Tuples
for item in multi_element_tuple:
    print("Tuple item:", item)

# 9. Tuple Methods
sample_tuple = (5, 1, 2, 1, 3)
print("Count of 1:", sample_tuple.count(1))
print("Index of 3:", sample_tuple.index(3))

# 10. Tuple Packing and Unpacking
packed = 10, 20, 30
a, b, c = packed
print("Packed tuple:", packed)
print("Unpacked values:", a, b, c)

# 11. Nested Tuples
nested = ((1, 2), (3, 4))
print("Nested tuple:", nested)
print("Access nested element:", nested[1][0])

# 12. Using Tuples as Dictionary Keys
d = {('x', 1): "value1", ('y', 2): "value2"}
print("Dictionary with tuple keys:", d)

# 13. Tuple vs List
# Tuples are immutable, lists are mutable
list_example = [1, 2, 3]
try:
    list_example[0] = 99  # This works
    print("Modified list:", list_example)
except Exception as e:
    print(e)

# Summary
print("""
Tuples are immutable sequences in Python.
They support indexing, slicing, concatenation, repetition, and can be used as dictionary keys.
Tuples are useful for fixed collections of items.
""")