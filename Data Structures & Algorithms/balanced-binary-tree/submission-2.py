class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ### Recursive solution
    #     # compute left height and right height and check difference
    #     if not root: return True
    #     left_height = self.maxHeight(root.left)
    #     right_height = self.maxHeight(root.right)
    #     difference = abs(left_height - right_height)
    #     # check that each subtree is also balanced
    #     return difference < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # def maxHeight(self, root: Optional[TreeNode]) -> int:
    #     if not root: return 0
    #     return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
    
        ### DFS Solution:
        if not root: return True
        balanced = True
        
        def dfs(root) -> int:
            nonlocal balanced

            if not root: return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            if abs(left_height - right_height) >= 2: 
                balanced = False
            return 1 + max(left_height, right_height)

        dfs(root)
        return balanced
            

