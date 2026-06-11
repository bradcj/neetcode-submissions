class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ### Recursive DFS:
        # if not p and not q: return True
        # if (not p and q) or (p and not q): return False
        # if p.val != q.val: return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        ### Iterative DFS:
        stack = deque([(p, q)])
        while stack:
            p, q = stack.pop()
            if (not p and q) or (p and not q): 
                return False
            if p and q:
                if p.val != q.val: return False
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
        
        return True
            

            
