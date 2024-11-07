class Node:
    """
    A class representing a node in a binary tree.

    Attributes:
    -----------
    key : int
        The value stored in the node.
    left : Node
        The left child of the node.
    right : Node
        The right child of the node.
    """

    def __init__(self, key):
        """
        Initializes a new node with the given key.

        Parameters:
        -----------
        key : int
            The value to be stored in the node.
        """
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    """
    A class representing a binary tree.

    Attributes:
    -----------
    root : Node
        The root node of the binary tree.
    """

    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def insert(self, key):
        """
        Inserts a new node with the given key into the binary tree.

        Parameters:
        -----------
        key : int
            The value to be inserted into the binary tree.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        """
        Helper method to insert a new node with the given key into the binary tree.

        Parameters:
        -----------
        node : Node
            The current node in the binary tree.
        key : int
            The value to be inserted into the binary tree.
        """
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        """
        Searches for a node with the given key in the binary tree.

        Parameters:
        -----------
        key : int
            The value to be searched in the binary tree.

        Returns:
        --------
        Node
            The node with the given key if found, otherwise None.
        """
        return self._search(self.root, key)

    def _search(self, node, key):
        """
        Helper method to search for a node with the given key in the binary tree.

        Parameters:
        -----------
        node : Node
            The current node in the binary tree.
        key : int
            The value to be searched in the binary tree.

        Returns:
        --------
        Node
            The node with the given key if found, otherwise None.
        """
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        """
        Performs an inorder traversal of the binary tree.

        Returns:
        --------
        list
            A list of keys representing the inorder traversal of the binary tree.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """
        Helper method to perform an inorder traversal of the binary tree.

        Parameters:
        -----------
        node : Node
            The current node in the binary tree.
        result : list
            A list to store the keys of the nodes in inorder traversal.
        """
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)


# Example usage of the BinaryTree class

# Create a new binary tree
tree = BinaryTree()

# Insert elements into the binary tree
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

# Search for elements in the binary tree
print(tree.search(7))  # Output: <__main__.Node object at ...>
print(tree.search(20))  # Output: None

# Perform an inorder traversal of the binary tree
print(tree.inorder_traversal())  # Output: [3, 5, 7, 10, 12, 15, 18]
