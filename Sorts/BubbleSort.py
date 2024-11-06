def bubble_sort(arr):
    """
    Sorts an array of numbers in ascending order using the bubble sort algorithm.

    The bubble sort algorithm works by repeatedly stepping through the list,
    comparing adjacent elements and swapping them if they are in the wrong order.
    This process is repeated until the list is sorted.

    Parameters:
    arr (list): The list of numbers to be sorted.

    Returns:
    None: The function sorts the list in place and does not return anything.

    Example:
    >>> numbers = [64, 34, 25, 12, 22, 11, 90]
    >>> bubble_sort(numbers)
    >>> print(numbers)
    [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print(numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
