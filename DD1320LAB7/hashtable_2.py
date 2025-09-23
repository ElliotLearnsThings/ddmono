import math


class HashNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.node_store = [None for _ in range(self.size)]

    def hashfunction(self, key, length):
        return math.floor(sum([ord(c) for c in str(key)])) % length

    def search(self, key):
        hash = self.hashfunction(key, self.size)
        node = self.node_store[hash]

        def check_node(node):
            if node.next is None:
                raise KeyError
            if node.key == key:
                return None
            else:
                return node.next

        while True:
            next_node = check_node(node)
            if not next_node:
                return node.val
            else:
                node = next_node

    def store(self, key, val):
        hash = self.hashfunction(key, self.size)
        position = self.node_store[hash]
        node = HashNode(key, val)
        if position is None:
            self.node_store[hash] = node
            return

        while True:
            if position.key == key:
                position.val = val
                return

            next_position = position.next
            if next_position is None:
                position.next = node
                return
            position = next_position


