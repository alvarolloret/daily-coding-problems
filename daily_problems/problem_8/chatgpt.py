class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_unival_subtrees(root):
    count = 0

    def is_unival(node):
        nonlocal count

        # Base case: If the node is None, return True
        if not node:
            return True
        left_unival = is_unival(node.left)
        right_unival = is_unival(node.right)

        # Check if the current node forms a unival subtree
        if left_unival and right_unival:
            if (node.left is None or node.left.val == node.val) and (
                node.right is None or node.right.val == node.val
            ):
                count += 1
                return True

        return False

    is_unival(root)
    return count


# Example tree
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(2)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(1)

# Count the number of unival subtrees
result = count_unival_subtrees(root)
print("Number of unival subtrees:", result)
