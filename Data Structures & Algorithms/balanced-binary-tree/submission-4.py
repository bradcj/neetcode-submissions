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
        # if not root: return True
        # balanced = True
        
        # def dfs(root) -> int:
        #     nonlocal balanced

        #     if not root: return 0
        #     left_height = dfs(root.left)
        #     right_height = dfs(root.right)
        #     if abs(left_height - right_height) >= 2: 
        #         balanced = False
        #     return 1 + max(left_height, right_height)

        # dfs(root)
        # return balanced
    
        ### Iterative DFS solution:
        if not root: return True
        stack = deque([root])
        heights = {}
        while stack:
            node = stack[-1]
            if node.left and node.left not in heights:
                stack.append(node.left)
            elif node.right and node.right not in heights:
                stack.append(node.right)
            else:
                node = stack.pop()
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)
                if abs(left_height - right_height) > 1:
                    return False
                heights[node] = 1 + max(left_height, right_height)
        
        return True

