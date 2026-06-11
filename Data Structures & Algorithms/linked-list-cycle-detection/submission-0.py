class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        node = head
        while node:
            if node in seen:
                return True
            seen.add(node)
            node = node.next
            
        return False
        
