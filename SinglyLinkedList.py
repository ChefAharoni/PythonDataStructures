class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Link the new node to the former head
        self.head = new_node  # Update the head to new node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node  # Append at the end

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_beginning(2)
llist.insert_at_end(3)
llist.traverse()  # Output: 2 -> 1 -> 3 -> None
