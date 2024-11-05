def quick_sort(arr):
    _quick_sort_helper(arr, 0, len(arr) - 1)


def _quick_sort_helper(arr, low, high):
    if low < high:
        # pi is partitioning index
        pi = _partition(arr, low, high)
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)


def _partition(arr, low, high):
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
