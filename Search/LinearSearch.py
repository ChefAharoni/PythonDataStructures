def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Target found
    return -1  # Target not found


# Example usage:
numbers = [4, 2, 5, 1, 3]
print(linear_search(numbers, 5))  # Output: 2
