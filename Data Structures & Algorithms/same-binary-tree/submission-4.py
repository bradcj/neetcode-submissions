class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ### Recursive DFS:
        # if not p and not q: return True
        # if (not p and q) or (p and not q): return False
        # if p.val != q.val: return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        ### Iterative DFS:
        # stack = deque([(p, q)])
        # while stack:
        #     p, q = stack.pop()
        #     if (not p and q) or (p and not q): 
        #         return False
        #     if p and q:
        #         if p.val != q.val: return False
        #         stack.append((p.left, q.left))
        #         stack.append((p.right, q.right))
        
        # return True
        
        ### BFS:
        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()
            if not p_node and not q_node:
                continue
            if (p_node and not q_node) or (not p_node and q_node) or p_node.val != q_node.val:
                return False

            p_queue.append(p_node.left)
            p_queue.append(p_node.right)
            q_queue.append(q_node.left)
            q_queue.append(q_node.right)
        
        return len(p_queue) == len(q_queue)
                
            
