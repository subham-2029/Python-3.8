# Python Program: Detailed Explanation of Dictionary Functions

def explain_dictionary_functions():
    print("Python Dictionary Functions Explained\n")

    # Creating a dictionary
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    print("Original Dictionary:", my_dict)

    # 1. len(): Get number of items
    print("\n1. len():")
    print("Length of dictionary:", len(my_dict))

    # 2. keys(): Get all keys
    print("\n2. keys():")
    print("Keys:", list(my_dict.keys()))

    # 3. values(): Get all values
    print("\n3. values():")
    print("Values:", list(my_dict.values()))

    # 4. items(): Get all key-value pairs
    print("\n4. items():")
    print("Items:", list(my_dict.items()))

    # 5. get(): Get value for a key (returns None if key not found)
    print("\n5. get():")
    print("Get 'name':", my_dict.get('name'))
    print("Get 'country' (not present):", my_dict.get('country'))

    # 6. update(): Update dictionary with another dictionary
    print("\n6. update():")
    my_dict.update({'age': 26, 'country': 'USA'})
    print("After update:", my_dict)

    # 7. pop(): Remove item by key and return its value
    print("\n7. pop():")
    age = my_dict.pop('age')
    print("Popped 'age':", age)
    print("After pop:", my_dict)

    # 8. popitem(): Remove and return last inserted key-value pair
    print("\n8. popitem():")
    item = my_dict.popitem()
    print("Popped item:", item)
    print("After popitem:", my_dict)

    # 9. setdefault(): Get value for key, insert if not present
    print("\n9. setdefault():")
    city = my_dict.setdefault('city', 'Unknown')
    print("Set default for 'city':", city)
    print("Set default for 'zip':", my_dict.setdefault('zip', '10001'))
    print("After setdefault:", my_dict)

    # 10. clear(): Remove all items
    print("\n10. clear():")
    my_dict.clear()
    print("After clear:", my_dict)

if __name__ == "__main__":
    explain_dictionary_functions()