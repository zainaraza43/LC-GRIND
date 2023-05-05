# Given the root of a binary tree, invert the tree, and return its root.

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Explanation
# We first start by checking if the the root is none since a node with no children cannot be inverted. This is our base case.
# Then we swap the left and right nodes for the current root
# Then we make a recursive call to all the left nodes
# Once all the recursive instances of the left nodes are terminated, we make the instances of the right nodes
# Once those are terminated, we return root
