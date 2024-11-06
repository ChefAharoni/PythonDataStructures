class TreeNode:
    """
    A class used to represent a Node in a Binary Tree.
    Attributes
    ----------
    value : any
        The value stored in the node.
    left : TreeNode, optional
        A reference to the left child node (default is None).
    right : TreeNode, optional
        A reference to the right child node (default is None).
    Methods
    -------
    __init__(self, value):
        Initializes the TreeNode with a value and optional left and right children.
    """
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Preorder Traversal: Root -> Left -> Right
def preorder(root):
    """
    Perform a preorder traversal of a binary tree.
    In a preorder traversal, the nodes are recursively visited in this order:
    1. Visit the root node.
    2. Traverse the left subtree.
    3. Traverse the right subtree.
    Args:
        root (TreeNode): The root node of the binary tree.
    Returns:
        None
    """

    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


# Inorder Traversal: Left -> Root -> Right
def inorder(root):
    """
    Perform an in-order traversal of a binary tree.
    An in-order traversal visits the nodes of the tree in the following order:
    1. Traverse the left subtree.
    2. Visit the root node.
    3. Traverse the right subtree.
    Args:
        root (TreeNode): The root node of the binary tree.
    Returns:
        None
    """

    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


# Postorder Traversal: Left -> Right -> Root
def postorder(root):
    """
    Perform a postorder traversal of a binary tree.
    In postorder traversal, the nodes are recursively visited in this order:
    1. Left subtree
    2. Right subtree
    3. Root node
    Args:
        root (Node): The root node of the binary tree.
    Returns:
        None: This function prints the value of each node during the traversal.
    """

    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


# Example usage:
# Creating a simple tree:
#      1
#     / \
#    2   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("Preorder traversal:")
preorder(root)  # Output: 1 2 3

print("\nInorder traversal:")
inorder(root)  # Output: 2 1 3

print("\nPostorder traversal:")
postorder(root)  # Output: 2 3 1
