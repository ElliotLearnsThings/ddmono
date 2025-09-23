class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"Node with value: {self.value}"
    
    def return_next(self):
        return self.next
    
    def add_next_node(self, newnode):
        self.next = newnode

class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        elements = []
        if self.first is None:
            return "Empty linked list"
        if self.first == self.last:
            return f"[{self.first.value}]"

        cur_node = self.first
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

        node = self.first

        if node is None:
            raise IndexError("Invalid indexing on empty linked list")

        node
        for _ in range(index):
            next_node = node.next
            if next_node is None:
                raise IndexError("Invalid index or damaged list")
            node = next_node

        return node

    def __getitem__(self, index):
        if index >= self.length or index < -self.length:
            return index
        if index < 0:
            index = self.length + index

        node = self.first

        if node is None:
            raise IndexError("Invalid indexing on empty linked list")

        for _ in range(index):
            next_node = node.next
            if next_node is None:
                raise IndexError("Invalid index or damaged list")
            node = next_node

        return node.value

    def is_empty(self):
        return self.length == 0

    def get_first(self):
        return self.first.value

    def get_last(self):
        return self.last.value

    def get_all(self): # This is ineffificent, the to_list method is O(n) while this is O(n^2)
        return [self[i] for i in range(self.length)]

    def __handle_insert(self, val, index = 0):
        if index >= self.length:
            self.enqueue(val)
            self.length -= 1
            return

        if index == 0:
            old_first = self.first
            new_node = Node(val, old_first)
            self.first = new_node
            return

        node_before = self.__getnode(index - 1)
        node_after = node_before.next
        new_node = Node(val, node_after)
        node_before.add_next_node(new_node)

    def insert(self, val, index = 0):
        self.__handle_insert(val, index)
        self.length += 1
        return

    def __handle_pop(self, index = -1):
        if index == 0:
            return self.dequeue()

        is_last = index == self.length - 1 or index == -1

        if is_last:
            if self.length == 1:
                last_node_value = self.last.value
                self.last = None
                self.first = None
                return last_node_value

            new_last_node = self.__getnode(self.length - 2)

            last_node_value = self.last.value
            self.last = new_last_node
            self.last.next = None # remove reference
            return last_node_value

        before_node = self.__getnode(index - 1)
        cur_node = before_node.next
        after_node = cur_node.next
        before_node.add_next_node(after_node)
        return cur_node.value

    def pop(self, index = -1):
        val = self.__handle_pop(index)
        self.length -= 1
        return val

    def to_list(self):
        elements = []
        cur_node = self.first
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
        if self.first == None:
            self.first = node
            self.last = node
        else:
            last_node = self.last
            last_node.add_next_node(node)
            self.last = node
    
    def dequeue(self):
        self.length -= 1
        if self.first == None:
            return None
        if self.first == self.last:
            node = self.last
            self.first = None
            self.last = None
            return node.value
        node = self.first
        nextnode = node.next
        self.first = nextnode
        return node.value


class TrollKarlen():

    def __init__(self, type):
        self.constructor = LinkedQ

    def find_forward(self, input):
        new_array = self.constructor()
        iterations = len(input)
        for i in range(iterations):
            x = input.pop(0)
            input.append(x)
            y = input.pop(0)
            new_array.enqueue(y)
        return new_array

    def find_reverse(self, input):
        reversearray = self.constructor()
        input.reverse()
        for val in input:
            reversearray.insert(val, 0)
            x = reversearray.pop(-1)
            reversearray.insert(x, 0)
        return reversearray


def get_user_input():
    try:
        return [x for x in input().split(" ")]
    except ValueError:
        print("Invalid input, try again")
        return get_user_input()

def run_troll_karlen(type = ""):
    user_input = get_user_input()
    tk = TrollKarlen(type)

    original_array = tk.find_forward(user_input)
    print (str(original_array.get_all()).replace("[", "").replace("]", "").replace(",", "").replace("'", "").strip())

def main():
    run_troll_karlen()
    
if __name__ == "__main__":
    main()
