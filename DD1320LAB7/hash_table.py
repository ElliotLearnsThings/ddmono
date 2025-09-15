import math
from typing import Callable, Generic, Protocol, TypeVar, override


class SupportsStringRepresentation(Protocol):
    @override
    def __str__(self, /) -> str: 
        ...

T = TypeVar("T")

class _HashNode(Generic[T]):
    
    def __init__(self, key, val: T | None, length: int, hash_funcs: list[Callable[[str], int]]) -> None:
        self.key: str = str(key)
        self.val: T | None = val
        self.length = length
        self._hash_funcs: list[Callable[[str], int]] = hash_funcs

    @override
    def __hash__(self) -> int:
        return math.floor(sum([func(self.key) for func in self._hash_funcs]) % self.length)

class HashTable(Generic[T]):
    def __init__(self, length: int, hash_funcs: list[Callable[[str], int]] | None = None, autoscale_breakpoint: float | None = None) -> None:
        self.length = length
        self.node_store: list[None | _HashNode[T]] = [None for _ in range(length)]
        self.capacity: int = length
        default_autoscale_breakpoint = 0.4
        self.autoscale_breakpoint: float = autoscale_breakpoint if autoscale_breakpoint != None and 0 < autoscale_breakpoint and 1 > autoscale_breakpoint else default_autoscale_breakpoint
        self.hash_funcs: list[Callable[[str], int]] = hash_funcs if hash_funcs != None else [
            lambda key: sum([ord(c) for c in key]) * len(key),
            lambda key: sum([ord(c) * i for (i, c) in enumerate(key)]),
            lambda key: sum([ord(c) * i if i % 2 == 0 else 1 for (i, c) in enumerate(key)]),
            lambda key: sum([ord(c) * i * 89 for (i, c) in enumerate(key)]),
                ]

    def __auto_scale(self):
        if self.capacity/self.length < self.autoscale_breakpoint:
            print(f"Warning, length leading to singular hashtable, autoscaling length to {self.length * 10}")
            self.length = self.length * 10
            self.capacity = self.length
            new_store: list[None | _HashNode[T]] = [None for _ in range(int(self.length))]

            for node in self.node_store:
                if node is not None:
                    self.store(node.key, node.val, new_store)

            self.node_store = new_store
            #print(f"Updated node_store with length: {len(self.node_store)}")

    def __handle_store(self, key: SupportsStringRepresentation, val: T | None, nodehash: int, node: _HashNode[T], store: list[_HashNode[T] | None]):

        current_node = store[nodehash]
            
        if current_node == None:
            self.capacity -= 1
            store[nodehash] = node

        if current_node != None and key == current_node.key:
            if val is None:
                self.capacity += 1
                current_node = None
                return
            else:
                store[nodehash] = node

        if current_node != None and key != current_node.key:
            print(current_node.key, current_node.val, "found with hash", nodehash)
            i = 0
            while i + nodehash + 1 < self.length:
                i += 1
                print("searching", nodehash + 1)
                next_node = store[nodehash + i]
                if next_node is not None and key == next_node.key:
                    next_node.val = val
                    print("updated value for hash at:", nodehash + i)
                    return
                if next_node == None:
                    store[nodehash + i] = node
                    print("key:", key, "set node for hash at:", nodehash + i)
                    return


    def store(self, key: SupportsStringRepresentation, val: T | None, store: list[_HashNode[T] | None] | None = None):
        store = store if store != None else self.node_store
        node = _HashNode(str(key), val, self.length, self.hash_funcs)
        nodehash = hash(node)
        self.__handle_store(str(key), val, nodehash, node, store)
        self.__auto_scale()

    def __handle_search(self, nodehash: int, key: SupportsStringRepresentation) -> T | None:
        if (node := self.node_store[nodehash]) != None and node.key == key:
            return node.val 
        if node is None:
            print("key", key, "found None with nodehash", nodehash)
            raise KeyError
        else:
            return self.__handle_search(nodehash + 1, str(key)) if nodehash + 1 < len(self.node_store) else None

    def search(self, key: SupportsStringRepresentation) -> T | None:
        if (node := self.node_store[hash_val := (hash(_HashNode(str(key), None, self.length, self.hash_funcs)))]) != None and node.key == key:
            return node.val 
        if node is None:
            raise KeyError
        else: 
            return self.__handle_search(hash_val + 1, key)

    def __contains__(self, key: SupportsStringRepresentation) -> bool:
        return self.node_store[hash(_HashNode(str(key), None, self.length, self.hash_funcs))] != None

    def __getitem__(self, key: SupportsStringRepresentation) -> T | None:
        return self.search(str(key))

