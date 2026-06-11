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

        ### DFS solution O(n):
        # diameter = 0

        # def dfs(root):
        #     nonlocal diameter

        #     if not root: return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     diameter = max(diameter, left + right)
        #     return 1 + max(left, right)

        # dfs(root)
        # return diameter
    
        ### Iterative DFS solution:
        if not root: return 0

        stack = deque([root])
        mp = {None: (0, 0)} # map to store (height, diameter) of each node
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                
                left_height, left_diameter = mp[node.left]
                right_height, right_diameter = mp[node.right]

                mp[node] = (1 + max(left_height, right_height),
                            max(left_height + right_height, left_diameter, right_diameter))
        
        return mp[root][1] # return max diameter from root
        
        



