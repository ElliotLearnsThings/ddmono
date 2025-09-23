import math

class _HashNode():
    def __init__(self, key, val):
        self.key = str(key)
        self.val = val

def myhash(node, length):
    sum = 0
    for c in node.key:
        sum += ord(c)

    size = sum // 10
    val = sum / length
    val = math.floor(val % 1 * size)
    return val % length


class Hashtable():
    def __init__(self, size, autoscale_breakpoint = None):
        self.size = size
        self.node_store = [None for _ in range(size * 10)]
        self.capacity = size
        default_autoscale_breakpoint = 0.4
        self.autoscale_breakpoint = autoscale_breakpoint if autoscale_breakpoint != None and 0 < autoscale_breakpoint and 1 > autoscale_breakpoint else default_autoscale_breakpoint

    def __auto_scale(self):
        if self.capacity/self.size < self.autoscale_breakpoint:
            print(f"Warning, size leading to singular hashtable, autoscaling size to {self.size * 10}")
            self.size = self.size * 10
            self.capacity = self.size
            new_store = [None for _ in range(int(self.size * 10))]

            for node in self.node_store:
                if node is not None:
                    self.store(node.key, node.val, new_store)

            self.node_store = new_store
            print(f"Updated node_store with size: {len(self.node_store)}")

    def __handle_store(self, key, val, nodehash, node, store):

        current_node = store[nodehash]
            
        if current_node == None:
            self.capacity -= 1
            store[nodehash] = node
            return

        if current_node != None and key == current_node.key:
            store[nodehash] = node
            return

        initial_nodehash, index = nodehash, nodehash
        while True:
            index = (index + 1) % self.size

            if index == initial_nodehash:
                self.__auto_scale()
                index = myhash(node, self.size)

            new_node = store[index]

            if new_node is None:
                self.capacity += 1
                store[index] = node
                return

            # Existing node with same key
            if new_node.key == key:
                new_node.val = val
                return


    def store(self, key, val, store = None):
        store = store if store != None else self.node_store
        node = _HashNode(str(key), val)
        nodehash = myhash(node, self.size)
        self.__handle_store(str(key), val, nodehash, node, store)

    def __handle_search(self, nodehash, key):

        initial_nodehash = nodehash
        while True:
            node = self.node_store[nodehash]

            if node is not None and node.key == key:
                return node.val

            if node is None:
                raise KeyError

            nodehash = (nodehash + 1) % self.size

            if nodehash == initial_nodehash:
                raise KeyError

            
    def hashfunction(self, key):
        return myhash(_HashNode(str(key), None))

    def search(self, key):
        if (node := self.node_store[hash_val := (myhash(_HashNode(str(key), None), self.size))]) != None and node.key == key:
            return node.val 
        if node is None:
            raise KeyError
        else: 
            return self.__handle_search(hash_val + 1, key)

    def __contains__(self, key):
        return self.node_store[myhash(_HashNode(str(key), None), self.size)] != None

    def __getitem__(self, key):
        return self.search(str(key))

