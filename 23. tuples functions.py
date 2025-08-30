# Python Program: Detailed Explanation of Tuple Functions

def explain_tuple_functions():
    print("Tuples in Python are immutable sequences, typically used to store collections of heterogeneous data.")
    print("\nCommon Tuple Functions and Methods:\n")

    # 1. len()
    t = (1, 2, 3, 4)
    print("1. len(tuple): Returns the number of elements in the tuple.")
    print(f"   Example: len({t}) = {len(t)}\n")

    # 2. count()
    t = (1, 2, 2, 3, 2)
    print("2. tuple.count(x): Returns the number of times x appears in the tuple.")
    print(f"   Example: {t}.count(2) = {t.count(2)}\n")

    # 3. index()
    t = ('a', 'b', 'c', 'b')
    print("3. tuple.index(x[, start[, end]]): Returns the first index of value x. Raises ValueError if not found.")
    print(f"   Example: {t}.index('b') = {t.index('b')}")
    print(f"   Example with start: {t}.index('b', 2) = {t.index('b', 2)}\n")

    # 4. min() and max()
    t = (5, 2, 8, 1)
    print("4. min(tuple) and max(tuple): Returns the smallest and largest item in the tuple.")
    print(f"   Example: min({t}) = {min(t)}")
    print(f"   Example: max({t}) = {max(t)}\n")

    # 5. sum()
    t = (1, 2, 3)
    print("5. sum(tuple): Returns the sum of all items in the tuple (if they are numbers).")
    print(f"   Example: sum({t}) = {sum(t)}\n")

    # 6. sorted()
    t = (3, 1, 2)
    print("6. sorted(tuple): Returns a sorted list from the tuple's items.")
    print(f"   Example: sorted({t}) = {sorted(t)}\n")

    # 7. tuple()
    l = [1, 2, 3]
    print("7. tuple(iterable): Converts an iterable (like a list) to a tuple.")
    print(f"   Example: tuple({l}) = {tuple(l)}\n")

    print("Note: Tuples do not support methods like append(), remove(), or pop() because they are immutable.")

if __name__ == "__main__":
    explain_tuple_functions()