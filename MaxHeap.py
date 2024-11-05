class MaxHeap:
    # Similar structure as MinHeap
    def __init__(self):
        self.heap = []

    # The rest of the methods are similar but with comparison operators adjusted
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    # ... (Other methods)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] < self.heap[index]:
            # Swap if parent is less than current
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    # Similar changes in _heapify_down
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
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
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)


# Example usage:
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(2)
max_heap.insert(15)
print(max_heap.peek())  # Output: 15
print(max_heap.extract_max())  # Output: 15
print(max_heap.peek())  # Output: 3
