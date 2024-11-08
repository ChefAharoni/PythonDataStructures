def merge_sort(arr):
    """
    Sorts an array in ascending order using the merge sort algorithm.

    Merge sort is a divide-and-conquer algorithm that splits the array into two halves,
    recursively sorts each half, and then merges the sorted halves back together.

    Args:
        arr (list): The list of elements to be sorted.

    Example:
        >>> numbers = [38, 27, 43, 3, 9, 82, 10]
        >>> merge_sort(numbers)
        >>> print(numbers)
        [3, 9, 10, 27, 38, 43, 82]
    """

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls to sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merging the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking for any remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage:
numbers = [38, 27, 43, 3, 9, 82, 10]
merge_sort(numbers)
print(numbers)  # Output: [3, 9, 10, 27, 38, 43, 82]
