class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"Node with value: {self.value}"
    
    def return_next(self):
        return self.next
    
    def add_next_node(self, newnode):
        self.next = newnode

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.length = 0

    def __str__(self):
        elements = []
        if self.__first is None:
            return "Empty linked list"
        if self.__first == self.__last:
            return f"[{self.__first.value}]"

        cur_node = self.__first
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
        return elements

    def enqueue(self, value):
        self.length += 1
        node = Node(value)
        if self.__first is None:
            self.__first = node
            self.__last = node
        else:
            last_node = self.__last
            last_node.add_next_node(node)
            self.__last = node
    
    def dequeue(self):
        if self.__first is None:
            return None
        self.length -= 1
        if self.__first == self.__last:
            node = self.__last
            self.__first = None
            self.__last = None
            return node.value
        node = self.__first
        nextnode = node.next
        self.__first = nextnode
        return node.value
    
    def peek(self):
        if self.__first is None:
            return None
        return self.__first.value
