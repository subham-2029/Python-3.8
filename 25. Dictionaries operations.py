# Python Program: Detailed Explanation of Dictionary Operations

# 1. Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Initial dictionary:", my_dict)

# 2. Accessing values
print("Name:", my_dict["name"])  # Using key directly
print("Age (using get):", my_dict.get("age"))  # Using get() method

# 3. Adding new key-value pairs
my_dict["email"] = "alice@example.com"
print("After adding email:", my_dict)

# 4. Updating values
my_dict["age"] = 31
print("After updating age:", my_dict)

# 5. Removing key-value pairs
removed_value = my_dict.pop("city")  # Removes 'city' and returns its value
print("Removed city:", removed_value)
print("After removing city:", my_dict)

# 6. Checking if a key exists
if "name" in my_dict:
    print("Key 'name' exists in dictionary.")

# 7. Iterating over keys
print("All keys:")
for key in my_dict.keys():
    print(key)

# 8. Iterating over values
print("All values:")
for value in my_dict.values():
    print(value)

# 9. Iterating over key-value pairs
print("All key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 10. Dictionary length
print("Number of items in dictionary:", len(my_dict))

# 11. Clearing the dictionary
my_dict.clear()
print("After clearing:", my_dict)

# 12. Copying a dictionary
original = {"a": 1, "b": 2}
copy_dict = original.copy()
print("Original:", original)
print("Copy:", copy_dict)

# 13. Nested dictionaries
nested_dict = {
    "person1": {"name": "Bob", "age": 25},
    "person2": {"name": "Carol", "age": 28}
}
print("Nested dictionary:", nested_dict)
print("Person1's name:", nested_dict["person1"]["name"])