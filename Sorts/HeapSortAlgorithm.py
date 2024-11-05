def heap_sort(arr):
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
