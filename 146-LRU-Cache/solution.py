class LRUCache:

    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity
        self.hash = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]  
            self._remove(node)
            self._add(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            node = Node(key, value)
            self.hash[key] = node
            self.count += 1
            self._add(node)
        else:
            node = self.hash[key]
            node.value = value
            self.get(key)
            
        if self.count > self.capacity:
            n = self.tail.prev
            self.hash.pop(n.key)
            self._remove(n)
            self.count -= 1
            
    def _connect(self, p, n):
        p.next, n.prev = n, p
        
    def _add(self, n):
        tmp = self.head.next
        self._connect(self.head, n)
        self._connect(n, tmp)
        
    def _remove(self, node):
        self._connect(node.prev, node.next)
        
        
        
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value =  value
        self.prev = None
        self.next = None
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
