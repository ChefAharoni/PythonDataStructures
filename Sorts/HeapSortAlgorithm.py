def heap_sort(arr):
    """
    Perform heap sort on a list of numbers.

    This function sorts a list in ascending order using the heap sort algorithm.
    It first builds a max-heap from the input list, then repeatedly extracts the
    maximum element from the heap and places it at the end of the list, reducing
    the heap size each time.

    Args:
        arr (list): The list of numbers to be sorted.

    Example:
        >>> numbers = [12, 11, 13, 5, 6, 7]
        >>> heap_sort(numbers)
        >>> print(numbers)
        [5, 6, 7, 11, 12, 13]

    """
    # Function implementation here
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)  # Heapify the reduced heap


def _heapify(arr, n, i):
    """
    Helper function to maintain the heap property.

    This function ensures that the subtree rooted at index `i` in a list `arr`
    of size `n` satisfies the max-heap property. If the subtree does not satisfy
    the max-heap property, it swaps elements to correct the property and
    recursively heapifies the affected subtree.

    Args:
        arr (list): The list representing the heap.
        n (int): The size of the heap.
        i (int): The index of the root of the subtree to heapify.

    Example:
        >>> arr = [4, 10, 3, 5, 1]
        >>> _heapify(arr, len(arr), 0)
        >>> print(arr)
        [10, 5, 3, 4, 1]
    """

    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # See if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        _heapify(arr, n, largest)  # Heapify the root


# Example usage:
numbers = [12, 11, 13, 5, 6, 7]
heap_sort(numbers)
print(numbers)  # Output: [5, 6, 7, 11, 12, 13]
