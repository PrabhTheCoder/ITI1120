class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
    def _connect(self, data):
        if len(data) > 0:
            self.next = Node(data[0])
            self.next._connect(data[1:])
    
class LinkedList:
        def __init__(self, items = []):
            if len(items) == 0:
                self.head = None
            else:
                self.head = Node(items[0])
                self.head._connect(items[1:])
        
        def print_list(self):
            next_node = self.head
            while(next_node):
                print(next_node.value)
                next_node = next_node.next
        def __repr__(self):
            s = ''
            next_node = self.head
            while(next_node):
                if len(s) == 0:
                    s += str(next_node.value)
                else:
                    s += "->" + str(next_node.value)
                next_node = next_node.next
            return s
