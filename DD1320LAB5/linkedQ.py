from typing import Generic, TypeVar, override

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T, next: 'Node[T] | None' = None):
        self.value: T = value
        self.next: None | Node[T] = next

    @override
    def __str__(self) -> str:
        return f"Node with value: {self.value}"
    
    def return_next(self):
        return self.next
    
    def add_next_node(self, newnode: 'Node[T] | None'):
        self.next = newnode



class LinkedQSimple(Generic[T]):
    def __init__(self):
        self.__first: None | Node[T] = None
        self.__last: None | Node[T] = None
        self.length: int = 0

    def __len__(self) -> int:
        return self.length

    @override
    def __str__(self):
        elements: list[Node[T]] = []
        if self.__first is None:
            return "Empty linked list"
        if self.__first == self.__last:
            return f"[{self.__first.value}]"

        cur_node: Node[T] = self.__first
        for _ in range(self.length):
            elements.append(cur_node)
            nextNode = cur_node.next
            if nextNode is None:
                break
            cur_node = nextNode

        outputString = "["

        for i, element in enumerate(elements):
            if i == len(elements) - 1:
                outputString += str(element.value)
                break
            outputString += str(element.value) + ", "

        return outputString + "]"


    @property
    def is_empty(self):
        return self.length == 0


    def enqueue(self, value: T):
        self.length += 1
        node: Node[T] = Node(value)
        if self.__first == None:
            self.__first = node
            self.__last = node
        else:
            first_node = self.__first
            node.add_next_node(first_node)
            self.__first = node
    
    def dequeue(self) -> T | None:
        if self.__first == None:
            return None

        self.length -= 1
        if self.__first == self.__last:
            node = self.__last
            self.__first = None
            self.__last = None
            return node.value if node is not None else None

        node = self.__first
        nextnode = node.next
        self.__first = nextnode
        return node.value


if __name__ == "__main__":
    new_linked_list: LinkedQSimple[int] = LinkedQSimple()
    new_linked_list.enqueue(1)
    new_linked_list.enqueue(2)
    print(new_linked_list.dequeue())
    print(new_linked_list.dequeue())
    [new_linked_list.enqueue(x) for x in range(10)]
    print(new_linked_list)
    my_int = new_linked_list.dequeue()
    print(new_linked_list)
