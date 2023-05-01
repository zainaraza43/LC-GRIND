class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)

            return max(ldepth + 1, rdepth + 1)
        
        return 0
