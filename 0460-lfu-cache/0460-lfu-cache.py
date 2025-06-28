import collections

# A Node class for our doubly linked list.
# It stores key, value, and frequency.
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

# A Doubly Linked List (DLL) class to manage a list of nodes.
# This list maintains LRU order *within a single frequency group*.
class DLinkedList:
    def __init__(self):
        # A DLL with sentinel head/tail nodes simplifies add/remove logic.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0  # We need to track the size of each list.

    def add_to_head(self, node: Node): # Add a node to the front (MRU).
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
        
    def remove_node(self, node: Node): # Remove a specific node from anywhere in the list.
        # This correctly unlinks the node by connecting its neighbors.
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def remove_tail(self) -> Node: # Remove the last node (LRU).
        if self.size == 0:
            return None
        # The node to remove is the one right before our dummy tail.
        node_to_remove = self.tail.prev
        self.remove_node(node_to_remove)
        return node_to_remove

class LFUCache:
    def __init__(self, capacity: int):
        # Enabled the capacity attribute.
        self.capacity = capacity
        self.key_map = {}  # The main map for O(1) key -> Node access.
        
        # This map groups nodes by frequency. Each frequency maps to a DLL of nodes.
        self.freq_map = collections.defaultdict(DLinkedList)
        
        # This variable tracks the lowest frequency currently in the cache.
        self.min_freq = 0

    def _update_node_freq(self, node: Node):
        """
        The core helper method. Called when a node is accessed.
        It moves the node from its old frequency list to the new one.
        """
        # 1. Get the node's current frequency and remove it from that frequency's DLL.
        old_freq = node.freq
        self.freq_map[old_freq].remove_node(node)
        
        # 2. If the old frequency's list is now empty and it was the minimum frequency,
        # we must update self.min_freq.
        if self.min_freq == old_freq and self.freq_map[old_freq].size == 0:
            self.min_freq += 1

        # 3. Increment the node's internal frequency count.
        node.freq += 1

        # 4. Add the updated node to the DLL of its new frequency.
        self.freq_map[node.freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
            
        node = self.key_map[key]
        self._update_node_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._update_node_freq(node)
        else: # This is a new key.
            if len(self.key_map) >= self.capacity:
                # Evict the LRU node from the minimum frequency list.
                lru_list = self.freq_map[self.min_freq]
                node_to_evict = lru_list.remove_tail()
                if node_to_evict:
                    del self.key_map[node_to_evict.key]
            
            # Create a new node and add it.
            new_node = Node(key, value) # freq defaults to 1
            self.key_map[key] = new_node
            self.freq_map[1].add_to_head(new_node)
            # A new item always has frequency 1, so reset the minimum frequency.
            self.min_freq = 1