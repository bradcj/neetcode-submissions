class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ### Recursive DFS solution:
        # if root is None: return root
        
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        
        # return root
        
        ### Iterative DFS solution:
        # if root is None: return root

        # stack = deque()
        # stack.append(root)
        
        # while len(stack) > 0:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left
        #     if node.left: stack.append(node.left)
        #     if node.right: stack.append(node.right)
        
        # return root
        
        ### BFS Solution:
        if root is None: return root
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        return root
            
            
