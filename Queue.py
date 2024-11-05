from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # Add item to the rear

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()  # Remove and return the front item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]  # Return the front item without removing it


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2
