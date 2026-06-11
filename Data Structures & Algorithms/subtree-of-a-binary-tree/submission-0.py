class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ### Recursive DFS:
        if not subRoot:
            return True
        if not root and subRoot:
            return False

        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q: 
                return True
            if (not p and q) or (p and not q) or p.val != q.val: 
                return False
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        
        if is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        

