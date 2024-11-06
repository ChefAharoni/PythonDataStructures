class Stack:
    """
    A simple implementation of a stack data structure.
    Attributes:
        items (list): The list to store stack items.
    Methods:
        __init__():
            Initializes an empty stack.
        is_empty() -> bool:
            Checks if the stack is empty.
        push(item):
            Adds an item to the top of the stack.
        pop() -> any:
            Removes and returns the top item of the stack. Returns None if the stack is empty.
        peek() -> any:
            Returns the top item of the stack without removing it. Returns None if the stack is empty.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)  # Add item to the top

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()  # Remove and return the top item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]  # Return the top item without removing it


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
print(stack.peek())  # Output: 1
