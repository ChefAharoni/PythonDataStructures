class ArrayList:
    """
    A dynamic array class akin to a simplified Python list.

    Attributes:
        capacity (int): The current capacity of the array.
        size (int): The number of elements in the array.
        array (list): The underlying array storing elements.
    """

    """
    Initializes an empty array list with an initial capacity of 1.
    """

    """
    Creates a new array with the given capacity.

    Args:
        capacity (int): The capacity of the new array.

    Returns:
        list: A new array with the specified capacity.
    """

    """
    Adds an item to the end of the array list. Resizes the array if necessary.

    Args:
        item: The item to be added to the array list.
    """

    """
    Resizes the array to a new capacity.

    Args:
        new_capacity (int): The new capacity of the array.
    """

    """
    Retrieves the item at the specified index.

    Args:
        index (int): The index of the item to retrieve.

    Returns:
        The item at the specified index.

    Raises:
        IndexError: If the index is out of bounds.
    """

    """
    Returns the number of elements in the array list.

    Returns:
        int: The number of elements in the array list.
    """

    """
    Returns a string representation of the array list.

    Returns:
        str: A string representation of the array list.
    """

    def __init__(self):
        self.capacity = 1  # Initial capacity
        self.size = 0  # Number of elements
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return [None] * capacity

    def append(self, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  # Double capacity if full
        self.array[self.size] = item
        self.size += 1

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of bounds")

    def __len__(self):
        return self.size

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"


# Example usage:
arr_list = ArrayList()
arr_list.append(1)
arr_list.append(2)
arr_list.append(3)
print(arr_list)  # Output: [1, 2, 3]
print(arr_list[1])  # Output: 2
print(len(arr_list))  # Output: 3
