class Node:
    def __init__(self, key, value):
        self.val, self.key = value, key
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cashe = dict()

        self.right, self.left = Node(0,0), Node(0,0)
        self.right.prev, self.left.next = self.left, self.right
    
    # insert the node at right side of the linked list
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt 

    # remove the node from the cashe
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key in self.cashe:
            self.remove(self.cashe[key])
            self.insert(self.cashe[key])
            return self.cashe[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cashe:
            self.remove(self.cashe[key])
        self.cashe[key] = Node(key, value)
        self.insert(self.cashe[key])

        if len(self.cashe) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cashe[lru.key]