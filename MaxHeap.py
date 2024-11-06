class MaxHeap:
    """
    A MaxHeap implementation where the largest element is always at the root.

    Attributes:
        heap (list): The list representation of the heap.
    """

    # Similar structure as MinHeap
    def __init__(self):
        """
        Initializes an empty MaxHeap.
        """
        self.heap = []

    # The rest of the methods are similar but with comparison operators adjusted
    def insert(self, key):
        """
        Inserts a new key into the heap.

        Args:
            key (int): The key to be inserted.
        """

        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """
        Ensures the heap property is maintained while inserting a new element.

        Args:
            index (int): The index of the newly inserted element.
        """

        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] < self.heap[index]:
            # Swap if parent is less than current
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    # Similar changes in _heapify_down
    def extract_max(self):
        """
        Extracts and returns the maximum element from the heap.

        Returns:
            int: The maximum element in the heap. Returns None if the heap is empty.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        """
        Ensures the heap property is maintained after extracting the root element.

        Args:
            index (int): The index of the element to heapify down.
        """

        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def peek(self):
        """
        Returns the maximum element in the heap without removing it.

        Returns:
            int: The maximum element in the heap. Returns None if the heap is empty.
        """

        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def size(self):
        """
        Returns the number of elements in the heap.

        Returns:
            int: The size of the heap.
        """

        return len(self.heap)


# Example usage:
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(2)
max_heap.insert(15)
print(max_heap.peek())  # Output: 15
print(max_heap.extract_max())  # Output: 15
print(max_heap.peek())  # Output: 3
