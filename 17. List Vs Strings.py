"""
List vs String in Python
------------------------

Both lists and strings are sequence types in Python, but they have important differences.

1. Definition:
    - List: A mutable sequence of elements, which can be of any type (integers, strings, objects, etc.).
    - String: An immutable sequence of Unicode characters.

2. Syntax:
    - List: Defined using square brackets []
      Example: my_list = [1, "apple", 3.14]
    - String: Defined using single or double quotes
      Example: my_string = "Hello, World!"

3. Mutability:
    - Lists are mutable. You can change, add, or remove elements.
      Example:
      my_list[0] = 42
      my_list.append("banana")
    - Strings are immutable. You cannot change characters in place.
      Example:
      # my_string[0] = "h"  # This will raise an error

4. Methods:
    - Lists have methods like append(), remove(), pop(), extend(), etc.
    - Strings have methods like lower(), upper(), replace(), split(), etc.

5. Iteration:
    - Both can be iterated using loops.
      Example:
      for item in my_list:
            print(item)
      for char in my_string:
            print(char)

6. Slicing:
    - Both support slicing.
      Example:
      print(my_list[1:3])
      print(my_string[0:5])

7. Use Cases:
    - Lists: Used for collections of items that may change.
    - Strings: Used for text data.

Example Code:
"""

# List example
my_list = [1, 2, 3]
my_list.append(4)        # [1, 2, 3, 4]
my_list[0] = 10          # [10, 2, 3, 4]
print("List:", my_list)

# String example
my_string = "hello"
# my_string[0] = "H"     # Error: strings are immutable
new_string = "H" + my_string[1:]  # "Hello"
print("String:", new_string)

# Slicing
print("List slice:", my_list[1:3])      # [2, 3]
print("String slice:", my_string[1:4])  # "ell"

# Iteration
for item in my_list:
     print("List item:", item)

for char in my_string:
     print("String char:", char)