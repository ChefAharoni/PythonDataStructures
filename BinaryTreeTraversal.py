class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Preorder Traversal: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


# Inorder Traversal: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


# Postorder Traversal: Left -> Right -> Root
def postorder(root):
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
