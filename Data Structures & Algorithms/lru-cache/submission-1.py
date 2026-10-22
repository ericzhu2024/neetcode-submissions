class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def _insert(self, node):
        prev, nxt = self.left, self.left.next
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt
    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.right.prev
            self._remove(lru)
            self.cache.pop(lru.key)
