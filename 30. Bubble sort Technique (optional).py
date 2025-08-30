# Bubble Sort Example in Python
# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
# compares adjacent elements and swaps them if they are in the wrong order.
# This process is repeated until the list is sorted.

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Print the array after each swap for illustration
                print(f"Swapped {arr[j]} and {arr[j+1]}: {arr}")
    return arr

# Example usage
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_list)
    sorted_list = bubble_sort(sample_list)
    print("Sorted list:", sorted_list)

# How Bubble Sort Works:
# 1. Start at the beginning of the list.
# 2. Compare the first two elements. If the first is greater than the second, swap them.
# 3. Move to the next pair and repeat step 2 until the end of the list.
# 4. After each pass, the largest element 'bubbles up' to its correct position.
# 5. Repeat the process for the remaining unsorted part of the list.
# 6. Continue until no swaps are needed, meaning the list is sorted.