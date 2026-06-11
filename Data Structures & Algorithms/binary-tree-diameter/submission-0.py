class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_height = self.maxHeight(root.left)
        right_height = self.maxHeight(root.right)
        diameter = left_height + right_height
        return max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
