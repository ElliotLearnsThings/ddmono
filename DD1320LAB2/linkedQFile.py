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

class LinkedQ:
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

    def __getnode(self, index):
        """
        Private method to get node at index
        """
        if index >= self.length or index < -self.length:
            index = self.length - 1
        if index < 0:
            index = self.length + index

        node = self.__first

        if node is None:
            raise IndexError("Invalid indexing on empty linked list")

        node: Node
        for _ in range(index):
            next_node = node.next
            if next_node is None:
                raise IndexError("Invalid index or damaged list")
            node = next_node

        return node

    @override
    def __getitem__(self, index):
        if index >= self.length or index < -self.length:
            return index
        if index < 0:
            index = self.length + index

        node = self.__first

        if node is None:
            raise IndexError("Invalid indexing on empty linked list")

        node: Node
        for _ in range(index):
            next_node = node.next
            if next_node is None:
                raise IndexError("Invalid index or damaged list")
            node = next_node

        return node.value

    @property
    def is_empty(self):
        return self.length == 0

    def get_first(self):
        return self.__first.value

    def get_last(self):
        return self.__last.value

    def get_all(self) -> list[Any]: # This is ineffificent, the to_list method is O(n) while this is O(n^2)
        return [self[i] for i in range(self.length)]

    def __handle_insert(self, val: Any, index: int = 0) -> None:
        if index >= self.length:
            self.enqueue(val)
            self.length -= 1
            return

        if index == 0:
            old_first = self.__first
            new_node = Node(val, old_first)
            self.__first = new_node
            return

        node_before = self.__getnode(index - 1)
        node_after = node_before.next
        new_node = Node(val, node_after)
        node_before.add_next_node(new_node)

    def insert(self, val: Any, index: int = 0) -> None:
        self.__handle_insert(val, index)
        self.length += 1
        return

    def __handle_pop(self, index: int = -1) -> Any:
        if index == 0:
            return self.dequeue()

        is_last = index == self.length - 1 or index == -1

        if is_last:
            if self.length == 1:
                last_node_value = self.__last.value
                self.__last = None
                self.__first = None
                return last_node_value

            new_last_node = self.__getnode(self.length - 2)

            last_node_value = self.__last.value
            self.__last = new_last_node
            self.__last.next = None # remove reference
            return last_node_value

        before_node = self.__getnode(index - 1)
        cur_node = before_node.next
        after_node = cur_node.next
        before_node.add_next_node(after_node)
        return cur_node.value

    def pop(self, index: int = -1) -> Any:
        val = self.__handle_pop(index)
        self.length -= 1
        return val

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
    new_linked_list = LinkedQ()
    new_linked_list.enqueue(1)
    new_linked_list.enqueue(2)
    print(new_linked_list.dequeue())
    print(new_linked_list.dequeue())
    [new_linked_list.enqueue(x) for x in range(10)]
    print(new_linked_list)
    print(new_linked_list[5])
    print(new_linked_list[-5])
    print(new_linked_list.pop(5))
    print(new_linked_list)
    print(new_linked_list.insert(5, 5))
    print(new_linked_list)
    print(new_linked_list.pop())
    print(new_linked_list)
