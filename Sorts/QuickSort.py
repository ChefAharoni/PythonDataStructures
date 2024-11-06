def quick_sort(arr):
    """
    Sorts an array in place using the QuickSort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    None
    """

    _quick_sort_helper(arr, 0, len(arr) - 1)


def _quick_sort_helper(arr, low, high):
    """
    Helper function for the QuickSort algorithm that recursively sorts sub-arrays.

    Parameters:
    arr (list): The list of elements to be sorted.
    low (int): The starting index of the sub-array to be sorted.
    high (int): The ending index of the sub-array to be sorted.

    Returns:
    None
    """

    if low < high:
        # pi is partitioning index
        pi = _partition(arr, low, high)
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)


def _partition(arr, low, high):
    """
    Partitions the array around a pivot element and returns the index of the pivot.

    Parameters:
    arr (list): The list of elements to be partitioned.
    low (int): The starting index of the sub-array to be partitioned.
    high (int): The ending index of the sub-array to be partitioned.

    Returns:
    int: The index of the pivot element after partitioning.
    """

    pivot = arr[high]  # Pivot
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  # Increment index
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot
    return i + 1


# Example usage:
numbers = [10, 7, 8, 9, 1, 5]
quick_sort(numbers)
print(numbers)  # Output: [1, 5, 7, 8, 9, 10]
