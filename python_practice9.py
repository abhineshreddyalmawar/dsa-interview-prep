# PHASE B - DAY 3 (Aug 3, 2026) | Trees & Recursion
# Real-world tie-in: Amtrak route hub branching to multiple cities; CCA-F link - BST in-order = sorted = DB indexes

# --- TreeNode : value + LEFT and RIGHT child pointers (binary tree = max 2 children) ---
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

hub = TreeNode("New York")
hub.left = TreeNode("Trenton")
hub.right = TreeNode("Newark")
hub.left.left = TreeNode("Princeton")
hub.left.right = TreeNode("Hamilton")

# --- recursion : a function calling itself, with a BASE CASE to stop ---
# base case: if node is None, do nothing, just return (stops infinite recursion)

# --- pre-order : visit -> left -> right ---
def print_preorder(node):
    if node is None:
        return
    print(node.value)
    print_preorder(node.left)
    print_preorder(node.right)

print_preorder(hub)
# New York, Trenton, Princeton, Hamilton, Newark

# --- in-order : left -> visit -> right ---
def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.value)
    print_inorder(node.right)

print_inorder(hub)
# Princeton, Trenton, Hamilton, New York, Newark
# NOTE: in-order on a Binary SEARCH Tree gives SORTED output -- this is why DB indexes use B-trees

# --- post-order : left -> right -> visit ---
def print_postorder(node):
    if node is None:
        return
    print_postorder(node.left)
    print_postorder(node.right)
    print(node.value)

print_postorder(hub)
# Princeton, Hamilton, Trenton, Newark, New York