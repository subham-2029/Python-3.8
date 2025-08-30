def insertion_sort(arr):
    print("Initial array:", arr)
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        print(f"\nInserting {key} into the sorted part {arr[:i]}")
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print(f"Moved {arr[j]} to position {j + 1}")
            j -= 1
        arr[j + 1] = key
        print(f"Inserted {key} at position {j + 1}")
        print("Array now:", arr)
    print("\nSorted array:", arr)

# Example usage
if __name__ == "__main__":
    numbers = [12, 11, 13, 5, 6]
    insertion_sort(numbers)