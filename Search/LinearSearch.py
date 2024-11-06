def linear_search(arr, target):
    """
    Perform a linear search on a list to find the index of a target value.

    Args:
        arr (list): The list of elements to search through.
        target: The value to search for in the list.

    Returns:
        int: The index of the target value if found, otherwise -1.

    Example:
        >>> numbers = [4, 2, 5, 1, 3]
        >>> linear_search(numbers, 5)
        2

    The function iterates through each element in the list `arr`. If it finds
    an element that matches the `target`, it returns the index of that element.
    If the `target` is not found in the list, the function returns -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index  # Target found
    return -1  # Target not found


# Example usage:
numbers = [4, 2, 5, 1, 3]
print(linear_search(numbers, 5))  # Output: 2
