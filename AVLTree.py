class AVLNode:
    """
    A node in an AVL tree.
    Attributes:
        key (int): The value stored in the node.
        left (AVLNode): The left child of the node.
        right (AVLNode): The right child of the node.
        height (int): The height of the node in the tree.
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of node


def insert(root, key):
    """
    Inserts a key into the AVL tree and returns the new root of the tree.
    This function performs the standard BST insertion and then updates the 
    height of the ancestor nodes. After insertion, it checks the balance 
    factor of the nodes and performs the necessary rotations to maintain 
    the AVL property.
    Args:
        root (AVLNode): The root node of the AVL tree.
        key (int): The key to be inserted into the AVL tree.
    Returns:
        AVLNode: The new root of the AVL tree after insertion and balancing.
    """

    # Perform normal BST insertion
    if not root:
        return AVLNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Get balance factor
    balance = get_balance(root)

    # If node is unbalanced, perform rotations
    # Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    # Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root  # Return the (unchanged) node pointer


def left_rotate(z):
    """
    Perform a left rotation on the given node z.
    Args:
        z (Node): The node to perform the left rotation on.
    Returns:
        Node: The new root node after the rotation.
    The left rotation involves the following steps:
    1. Set y to be the right child of z.
    2. Set T2 to be the left child of y.
    3. Make y the new root by setting y's left child to z.
    4. Set z's right child to T2.
    5. Update the heights of z and y.
    """

    y = z.right
    T2 = y.left

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y  # Return new root


def right_rotate(z):
    """
    Perform a right rotation on the given node z.
    Args:
        z (Node): The root node of the subtree to be rotated.
    Returns:
        Node: The new root node of the subtree after rotation.
    The function performs a right rotation on the subtree rooted at node z.
    It updates the heights of the affected nodes and returns the new root
    of the subtree.
    """

    y = z.left
    T3 = y.right

    # Perform rotation
    y.right = z
    z.left = T3

    # Update heights
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y  # Return new root


def get_height(node):
    """
    Get the height of a given node in an AVL tree.
    Parameters:
    node (Node): The node whose height is to be retrieved.
    Returns:
    int: The height of the node. Returns 0 if the node is None.
    """

    if not node:
        return 0
    return node.height


def get_balance(node):
    """
    Calculate the balance factor of a given node in an AVL tree.
    The balance factor is defined as the difference between the height of the left subtree
    and the height of the right subtree. A balance factor of -1, 0, or 1 indicates that the
    tree is balanced at the given node.
    Parameters:
    node (Node): The node for which the balance factor is to be calculated.
    Returns:
    int: The balance factor of the node. Returns 0 if the node is None.
    """

    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def preorder_traversal(root):
    """
    Perform a preorder traversal of an AVL tree.
    In a preorder traversal, the nodes are recursively visited in this order:
    1. Visit the root node.
    2. Traverse the left subtree.
    3. Traverse the right subtree.
    Args:
        root (Node): The root node of the AVL tree.
    Returns:
        None
    """

    if root:
        print("{0} ".format(root.key), end="")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


# Example usage:
root = None
keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    root = insert(root, key)

print("Preorder traversal of the AVL tree is:")
preorder_traversal(root)  # Output: 30 20 10 25 40 50
