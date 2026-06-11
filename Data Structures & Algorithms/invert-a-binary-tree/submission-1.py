class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ### Recursive DFS solution:
        # if root is None: return root
        
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        
        # return root
        
        ### BFS solution:
        if root is None: return root

        queue = deque()
        queue.append(root)
        
        while len(queue) > 0:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        return root
            

        

        
        
