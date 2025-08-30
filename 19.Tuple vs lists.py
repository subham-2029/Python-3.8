import time

# Tuple vs List in Python

# 1. Definition
# List: Mutable, ordered collection of items.
# Tuple: Immutable, ordered collection of items.

# 2. Syntax
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)

print("List:", my_list)
print("Tuple:", my_tuple)

# 3. Mutability
# Lists can be changed after creation.
my_list[0] = 10
print("Modified List:", my_list)

# Tuples cannot be changed after creation.
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Tuple modification error:", e)

# 4. Methods
print("List methods:", dir(my_list))
print("Tuple methods:", dir(my_tuple))

# 5. Use Cases
# Lists: When you need a collection of items that may change.
# Tuples: When you need a collection of items that should not change (e.g., coordinates, fixed data).

# 6. Performance

list_start = time.time()
for i in range(1000000):
    a = [1, 2, 3, 4]
list_end = time.time()

tuple_start = time.time()
for i in range(1000000):
    b = (1, 2, 3, 4)
tuple_end = time.time()

print("List creation time:", list_end - list_start)
print("Tuple creation time:", tuple_end - tuple_start)

# 7. Packing and Unpacking
a, b, c = (1, 2, 3)
print("Tuple unpacking:", a, b, c)

# 8. Immutability Example
def try_modify_tuple(t):
    try:
        t[0] = 99
    except TypeError:
        print("Cannot modify tuple!")

try_modify_tuple((5, 6, 7))

# 9. Nested Structures
nested_list = [1, [2, 3], 4]
nested_tuple = (1, (2, 3), 4)
print("Nested List:", nested_list)
print("Nested Tuple:", nested_tuple)

# Summary
print("""
Summary:
- Lists are mutable, have more methods, and are suitable for dynamic data.
- Tuples are immutable, faster to create, and suitable for fixed data.
""")