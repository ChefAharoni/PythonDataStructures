from collections import deque

"""
A class used to represent a Queue.

Attributes
----------
items : deque
    a deque to store the elements of the queue

Methods
-------
is_empty():
    Checks if the queue is empty.
enqueue(item):
    Adds an item to the rear of the queue.
dequeue():
    Removes and returns the front item of the queue.
peek():
    Returns the front item of the queue without removing it.
"""


class Queue:
    def __init__(self):
        """
        Constructs all the necessary attributes for the Queue object.
        """

        self.items = deque()

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns
        -------
        bool
            True if the queue is empty, False otherwise.
        """

        return len(self.items) == 0

    def enqueue(self, item):
        """
        Adds an item to the rear of the queue.

        Parameters
        ----------
        item : any
            The item to be added to the queue.
        """

        self.items.append(item)  # Add item to the rear

    def dequeue(self):
        """
        Removes and returns the front item of the queue.

        Returns
        -------
        any
            The front item of the queue if the queue is not empty, None otherwise.
        """

        if self.is_empty():
            return None
        return self.items.popleft()  # Remove and return the front item

    def peek(self):
        """
        Returns the front item of the queue without removing it.

        Returns
        -------
        any
            The front item of the queue if the queue is not empty, None otherwise.
        """

        if self.is_empty():
            return None
        return self.items[0]  # Return the front item without removing it


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2
