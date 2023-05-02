from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root == None: return 0
        
        # l_dep = self.maxDepth(root.left)
        # r_dep = self.maxDepth(root.right)

        # return r_dep + 1 if l_dep < r_dep else l_dep + 1

        # Combining into one line
        return 0 if root == None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# Driver Code
if __name__ == "__main__":
    bTree = TreeNode(
        3,
        TreeNode(9, None, None),
        TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)),
    )

    print(Solution().maxDepth(bTree))
