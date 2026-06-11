class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        stack = deque()
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        
        head_dummy = ListNode()
        prev_node = head_dummy
        while stack:
            new_node = ListNode(stack.pop())
            prev_node.next = new_node
            prev_node = new_node
        
        return head_dummy.next
                        
