class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ### Recursive DFS solution:
        # if root is None: return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        ### Iterative DFS solution:
        # if root is None: return 0
        # stack = deque([(root, 1)])
        # max_depth = 0
        # while len(stack) > 0:
        #     node, depth = stack.pop()
        #     max_depth = max(max_depth, depth)
            
        #     if node.left: stack.append((node.left, depth + 1))
        #     if node.right: stack.append((node.right, depth + 1))
        
        # return max_depth
        
        ### BFS solution:
        queue = deque()
        if root: queue.append(root)
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            depth += 1
        
        return depth
                
            



