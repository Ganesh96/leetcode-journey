class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.least = Node(0, 0)
        self.most = Node(0, 0)
        self.least.next = self.most
        self.most.prev = self.least

    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insert(self, node):
        prevNode, nextNode = self.most.prev, self.most
        prevNode.next = node
        nextNode.prev = node
        node.prev = prevNode
        node.next = nextNode

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.cap:
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
