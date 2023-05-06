# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1
            
# Explanation
# Start with a base case to check if the tree/root/node is empty (can't have a path or extend it if it's empty)
# Recursively calculate the depth of the left side
# Recursively calculate the depth of the right side
# Compare the two to see which is larger and return the answer (+1 is to include the current node)
