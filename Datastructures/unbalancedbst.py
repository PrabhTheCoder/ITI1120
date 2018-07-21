#Binary Search Tree in Python
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
            
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    def pre_order(self):
        if self:
            print(self.value)
            if self.leftChild:
                self.leftChild.pre_order()
            if self.rightChild:
                self.rightChild.pre_order()
                
    def post_order(self):
        if self:
            if self.leftChild:
                self.leftChild.post_order()
            if self.rightChild:
                self.rightChild.post_order()
            print(self.value)
    def in_order(self):
        if self:
            if self.leftChild:
                self.leftChild.in_order()
            print(self.value)
            if self.rightChild:
                self.rightChild.in_order()
            
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def pre_order(self):
        print("PreOrder")
        self.root.pre_order()

    def post_order(self):
        print("PostOrder")
        self.root.post_order()

    def in_order(self):
        print("InOrder")
        self.root.in_order()
