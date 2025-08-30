# Python Program: Detailed Explanation of Dictionary Methods

def explain_dict_methods():
    # Creating a sample dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original Dictionary:", sample_dict)

    # 1. dict.keys()
    print("\n1. keys(): Returns a view object of all keys.")
    print("Keys:", sample_dict.keys())

    # 2. dict.values()
    print("\n2. values(): Returns a view object of all values.")
    print("Values:", sample_dict.values())

    # 3. dict.items()
    print("\n3. items(): Returns a view object of key-value pairs.")
    print("Items:", sample_dict.items())

    # 4. dict.get(key, default)
    print("\n4. get(key, default): Returns value for key, else default.")
    print("Get 'b':", sample_dict.get('b'))
    print("Get 'z' (not present):", sample_dict.get('z', 'Not Found'))

    # 5. dict.pop(key, default)
    print("\n5. pop(key, default): Removes key and returns value, else default.")
    popped_value = sample_dict.pop('a', 'Not Found')
    print("Popped 'a':", popped_value)
    print("Dictionary after pop:", sample_dict)

    # 6. dict.popitem()
    print("\n6. popitem(): Removes and returns last inserted key-value pair.")
    last_item = sample_dict.popitem()
    print("Popped item:", last_item)
    print("Dictionary after popitem:", sample_dict)

    # 7. dict.update(other_dict)
    print("\n7. update(other_dict): Updates dictionary with another dictionary.")
    sample_dict.update({'d': 4, 'e': 5})
    print("Dictionary after update:", sample_dict)

    # 8. dict.clear()
    print("\n8. clear(): Removes all items from dictionary.")
    sample_dict.clear()
    print("Dictionary after clear:", sample_dict)

    # 9. dict.copy()
    print("\n9. copy(): Returns a shallow copy of the dictionary.")
    new_dict = {'x': 10, 'y': 20}
    copied_dict = new_dict.copy()
    print("Original:", new_dict)
    print("Copy:", copied_dict)

    # 10. dict.setdefault(key, default)
    print("\n10. setdefault(key, default): Returns value if key exists, else inserts key with default.")
    print("Before setdefault:", copied_dict)
    value = copied_dict.setdefault('z', 30)
    print("Setdefault 'z':", value)
    print("After setdefault:", copied_dict)

if __name__ == "__main__":
    explain_dict_methods()