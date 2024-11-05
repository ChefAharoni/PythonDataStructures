import sys


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        root = self.heap[0]
        # Move the last element to root and heapify down
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] > self.heap[index]:
            # Swap and continue heapifying up
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Check if left child exists and is smaller than current
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Check if right child exists and is smaller than current smallest
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current index, swap and continue heapifying down
        if smallest != index:
            self.heap[smallest], self.heap[index] = (
                self.heap[index],
                self.heap[smallest],
            )
            self._heapify_down(smallest)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]


# Example usage:
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(15)
print(min_heap.get_min())  # Output: 2
print(min_heap.extract_min())  # Output: 2
print(min_heap.get_min())  # Output: 3
