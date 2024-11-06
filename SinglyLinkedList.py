class Node:
    """
    A class used to represent a Node in a Singly Linked List.
    Attributes
    ----------
    data : any
        The data stored in the node.
    next : Node or None
        The reference to the next node in the linked list.
    Methods
    -------
    __init__(self, data):
        Initializes the Node with the given data and sets the next reference to None.
    """

    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Reference to the next node


class LinkedList:
    """
    A class used to represent a Singly Linked List.
    ...
    Attributes
    ----------
    head : Node or None
        The head node of the linked list.
    Methods
    -------
    __init__():
        Initializes the linked list with an empty head.
    insert_at_beginning(data):
        Inserts a new node with the specified data at the beginning of the list.
    insert_at_end(data):
        Inserts a new node with the specified data at the end of the list.
    traverse():
        Traverses the linked list and prints the data of each node.
    """
    
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
