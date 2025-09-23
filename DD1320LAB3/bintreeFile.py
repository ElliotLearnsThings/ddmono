class Bintree:
    def __init__(self):
        self.root = None
        
    def putta(self, p, newvalue):
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

    def put(self, newvalue):
        newvalue = str(newvalue) 
        if self.root is None:
            self.root = Node(newvalue)
        else:
            self.putta(self.root, newvalue)
    
    def __contains__(self, value):
        value = str(value)
        return self._finns(self.root, value)

    def _finns(self, node, value):
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

    def skriv(self, node):
        if node is not None:
            self.skriv(node.left)
            print(node.value)
            self.skriv(node.right)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "Node"
