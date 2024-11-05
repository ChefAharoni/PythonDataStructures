class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of node


def insert(root, key):
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
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def preorder_traversal(root):
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
