from typing import Generic, Protocol, Self, TypeVar, override

class SupportsLessThan(Protocol):
    def __lt__(self, value: Self, /) -> bool: 
        ...

T = TypeVar("T", bound=SupportsLessThan)

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value
        self.left: 'None | Node[T]'  = None
        self.right: 'None | Node[T]' = None

    @override
    def __str__(self):
        return "Node"

class Bintree(Generic[T]):
    def __init__(self):
        self.root: 'None | Node[T]' = None
        self.length: int = 0

    def putta(self, p: 'Node[T]', newvalue: T):
        if newvalue == p.value:
            return  # värdet finns redan
        elif newvalue < p.value:
            if p.left is None:
                p.left = Node(newvalue)
            else:
                self.putta(p.left, newvalue)
        else:  # newvalue > p.value
            if p.right is None:
                p.right = Node(newvalue)
            else:
                self.putta(p.right, newvalue)

    def __handle_put(self, newvalue: T):
        newvalue = newvalue
        if self.root is None:
            self.root = Node(newvalue)
        else:
            self.putta(self.root, newvalue)

    def put(self, newvalue: T):
        self.__handle_put(newvalue)
        self.length += 1

    def __len__(self):
        return self.length
    
    def __contains__(self, value: T):
        return self._finns(self.root, value)

    def _finns(self, node: 'Node[T] | None', value: T) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._finns(node.left, value)
        else:
            return self._finns(node.right, value)

    def write(self): #skriv inorder
        self.skriv(self.root)
        print("\n")

    def skriv(self, node: Node[T] | None):
        if node is not None:
            self.skriv(node.left)
            print(node.value)
            self.skriv(node.right)

