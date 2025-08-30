

"""
Python List Functions Explained

This file demonstrates and explains all the major built-in list methods in Python.
"""

# 1. append(x)
# Adds an item x to the end of the list.
lst = [1, 2, 3]
lst.append(4)
print("append:", lst)  # [1, 2, 3, 4]

# 2. extend(iterable)
# Adds all elements from the iterable to the end of the list.
lst.extend([5, 6])
print("extend:", lst)  # [1, 2, 3, 4, 5, 6]

# 3. insert(i, x)
# Inserts item x at position i. Existing elements shift right.
lst.insert(2, 'a')
print("insert:", lst)  # [1, 2, 'a', 3, 4, 5, 6]

# 4. remove(x)
# Removes the first occurrence of x. Raises ValueError if not found.
lst.remove('a')
print("remove:", lst)  # [1, 2, 3, 4, 5, 6]

# 5. pop([i])
# Removes and returns item at index i (default last). Raises IndexError if empty.
item = lst.pop()
print("pop:", item, lst)  # 6 [1, 2, 3, 4, 5]

item = lst.pop(1)
print("pop at index 1:", item, lst)  # 2 [1, 3, 4, 5]

# 6. clear()
# Removes all items from the list.
lst.clear()
print("clear:", lst)  # []

# 7. index(x[, start[, end]])
# Returns first index of x. Raises ValueError if not found.
lst = [10, 20, 30, 20]
idx = lst.index(20)
print("index:", idx)  # 1

# 8. count(x)
# Returns number of occurrences of x.
cnt = lst.count(20)
print("count:", cnt)  # 2

# 9. sort(key=None, reverse=False)
# Sorts the list in place.
lst.sort()
print("sort:", lst)  # [10, 20, 20, 30]

lst.sort(reverse=True)
print("sort reverse:", lst)  # [30, 20, 20, 10]

# 10. reverse()
# Reverses the list in place.
lst.reverse()
print("reverse:", lst)  # [10, 20, 20, 30]

# 11. copy()
# Returns a shallow copy of the list.
lst2 = lst.copy()
print("copy:", lst2)  # [10, 20, 20, 30]

# Summary Table
"""
Method         | Description
---------------|---------------------------------------------------------
append(x)      | Add x to end of list
extend(iter)   | Add all elements from iterable
insert(i, x)   | Insert x at index i
remove(x)      | Remove first occurrence of x
pop([i])       | Remove and return item at index i (default last)
clear()        | Remove all items
index(x)       | Return first index of x
count(x)       | Count occurrences of x
sort()         | Sort list in place
reverse()      | Reverse list in place
copy()         | Shallow copy of list
"""