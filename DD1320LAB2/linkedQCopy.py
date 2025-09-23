from typing import Any, override


class Node:
    def __init__(self, value, next: 'Node | None' = None):
        self.value = value
        self.next: None | Node = next

    @override
    def __str__(self) -> str:
        return f"Node with value: {self.value}"
    
    def return_next(self):
        return self.next
    
    def add_next_node(self, newnode: 'Node | None'):
        self.next = newnode

class LinkedQSimple:
    def __init__(self):
        self.__first: None | Node = None
        self.__last: None | Node = None
        self.length = 0

    @override
    def __str__(self):
        elements = []
        if self.__first is None:
            return "Empty linked list"
        if self.__first == self.__last:
            return f"[{self.__first.value}]"

        cur_node: Node = self.__first
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

    def to_list(self):
        elements = []
        cur_node = self.__first
        if cur_node is None or self.length == 0:
            return []
        for _ in range(self.length):
            elements.append(cur_node)
            next_node = cur_node.next
            if next_node is None:
                raise IndexError("Damaged linked list object, found item without reference")
            cur_node = next_node
            

    def enqueue(self, value):
        self.length += 1
        node = Node(value)
        if self.__first == None:
            self.__first = node
            self.__last = node
        else:
            last_node = self.__last
            last_node.add_next_node(node)
            self.__last = node
    
    def dequeue(self):
        self.length -= 1
        if self.__first == None:
            return None
        if self.__first == self.__last:
            node = self.__last
            self.__first = None
            self.__last = None
            return node.value
        node = self.__first
        nextnode = node.next
        self.__first = nextnode
        return node.value


if __name__ == "__main__":
    new_linked_list = LinkedQSimple()
    new_linked_list.enqueue(1)
    new_linked_list.enqueue(2)
    print(new_linked_list.dequeue())
    print(new_linked_list.dequeue())
    [new_linked_list.enqueue(x) for x in range(10)]
    print(new_linked_list)
