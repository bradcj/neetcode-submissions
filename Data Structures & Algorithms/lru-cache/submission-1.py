class DoublyLinkedListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = {} # {key: node}
        self.capacity = capacity
        
        self.head = self.tail = None

    def _move_node_to_tail(self, node):
        if node == self.tail:
            return
        
        # move node to tail: re-wire prev and next neighbors
        if node == self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
        
        node.next.prev = node.prev

        node.prev = self.tail
        self.tail.next = node
        node.next = None

        self.tail = node
    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_node_to_tail(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_node_to_tail(node)
            return
        
        if len(self.cache) == self.capacity:
            # remove head node (least recently used)
            del self.cache[self.head.key]
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        
        node = DoublyLinkedListNode(key, value)
        # check if first node added to list
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # add node to tail
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.cache[key] = node

