# Introduction to Dictionaries in Python

# A dictionary is a collection of key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers).
# Values can be of any type.

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values using keys
print("Name:", person["name"])
print("Age:", person["age"])

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Updating a value
person["age"] = 31

# Removing a key-value pair
del person["city"]

# Iterating over keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "email" in person:
    print("Email is:", person["email"])