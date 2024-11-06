def binary_search(arr, target):
    """
    Perform a binary search on a sorted array to find the index of a target value.

    Args:
        arr (list): A list of elements sorted in ascending order.
        target: The value to search for in the array.

    Returns:
        int: The index of the target value in the array if found, otherwise -1.

    Example:
        >>> numbers = [1, 2, 3, 4, 5]
        >>> binary_search(numbers, 4)
        3

    The function works by repeatedly dividing the search interval in half. If the target value is less than the value
    in the middle of the interval, the search continues in the lower half. If the target value is greater, the search
    continues in the upper half. This process continues until the target value is found or the interval is empty.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    return -1  # Target not found


# Example usage:
numbers = [1, 2, 3, 4, 5]
print(binary_search(numbers, 4))  # Output: 3
