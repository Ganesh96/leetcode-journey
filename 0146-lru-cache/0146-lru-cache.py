# Helper class for the nodes in our doubly linked list.
class Node:
    def __init__(self, key, val):
        # The node needs to store the key and value to manage the hash map.
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Step 1: Initialize the core components.
        self.capacity = capacity
        # The hash map stores key -> Node mappings for O(1) access.
        self.cache = {} 
        
        # We use dummy head and tail nodes (sentinels) to make the
        # logic for adding/removing from the list ends simpler.
        # self.head is the Most Recently Used side of the list.
        # self.tail is the Least Recently Used side of the list.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- Private Helper Methods ---
    # A helper to remove a node from its current position in the list.
    def _remove_node(self, node: Node):
        # Unlink the node from its neighbors.
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # A helper to add a node to the front of the list (most recently used).
    def _add_to_front(self, node: Node):
        # Wire up the new node right after the dummy head.
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    # --- Public API Methods ---
    def get(self, key: int) -> int:
        # Step 1: Check if the key exists in our hash map cache.
        if key in self.cache:
            # Step 1a: If it exists, we need to mark it as most recently used.
            # We do this by moving its node to the front of the linked list.
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_front(node)
            return node.val
        # Step 2: If the key isn't in the cache, return -1.
        return -1

    def put(self, key: int, value: int) -> None:
        # Step 1: Check if the key already exists in the cache.
        if key in self.cache:
            # If it exists, update its value and mark it as most recently used.
            node = self.cache[key]
            node.val = value
            self._remove_node(node)
            self._add_to_front(node)
        else:
            # Step 2: If the key is new, first check if we are at capacity.
            if len(self.cache) >= self.capacity:
                # If yes, we must evict the least recently used item.
                # The LRU item is the node at the tail of our list.
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key] # Remove from hash map too.
            
            # Step 3: Add the new key-value pair.
            # Create a new node, add it to the front of the list,
            # and add it to the hash map.
            new_node = Node(key, value)
            self._add_to_front(new_node)
            self.cache[key] = new_node