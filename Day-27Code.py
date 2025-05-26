# Day 27 - Chaining timer + Log decorators for sorting function.
# topic - Chaining Decorators.

# Importing logger and timer decorators from Decorators.py
from Decorators import logger, timer

# Chaining the decorators (timer first, then logger)
@timer
@logger
def bubble_sort(arr):
    # Bubble sort algorithm
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# main
def main():
    # Test sorting function with sample ones
    test_array = [64, 34, 25, 12, 22, 11, 90]
    # Displaying original array.
    print(f"Original Array: {test_array}")
    # passing that array into bubble_sort() to sort it down
    sorted_array = bubble_sort(test_array)
    # Displaying sorted array result
    print(f"Sorted Array: {sorted_array}")

# calling main() to starting execution of program
if __name__ == "__main__":
    main()
