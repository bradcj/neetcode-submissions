class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ### Recursive brute-force solution O(n^2):
    #     if root is None:
    #         return 0
    #     left_height = self.maxHeight(root.left)
    #     right_height = self.maxHeight(root.right)
    #     diameter = left_height + right_height
    #     return max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    # def maxHeight(self, root: Optional[TreeNode]) -> int:
    #     if root is None: return 0
    #     return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

        ### DFS solution:
        diameter = 0

        def dfs(root):
            nonlocal diameter

            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return diameter


