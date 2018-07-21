class MinHeap:
    def __init__(self,  items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)
    def push(self, data):
        """(MinHeap, Object) -> None
            Pushes data into the heap.
        """
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
        
    def peek(self):
        """(MinHeap) -> Object
            Returns the minimum item in the heap
        """
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return False
    def pop(self):
        """(MinHeap) -> Object
            Returns and removes the minimum object in the heap.
        """
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1) #Swaps last element and min to allow popping in const time
            minimum = self.heap.pop()
            self.__minHeapify(1) #Puts everything back where it belongs
        elif len(self.heap) == 2:
            minimum = self.heap.pop()
        else:
            minimum = False
        return minimum
    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def __floatUp(self, index):
        parent = index // 2
        #reached top of heap so just return
        if index <= 1:
            return
        #if child is less than parent, swap them and perform same checks on the parent of the parent.
        elif self.heap[index] < self.heap[parent]: 
            self.__swap(index, parent)
            self.__floatUp(parent)
    def __minHeapify(self, index):
        left = index * 2 #left child
        right = index * 2 + 1 #right child
        smallest = index #initially assumes index is the largest

        #if left child exists, and the current smallest is greater than the left
        #child set the largest as the left childs index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        #if the right child exists, and the current smallest is  greater than
        #the right child set the largest as the right childs index.
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            #if the smallest isnt the current number, swap places with the smallest
            #and then perform same operations on the index the current item was
            #moved to.
            self.__swap(index, smallest)
            self.__minHeapify(smallest)


def find_minimum_loss(a):
    tmp = MinHeap()
    for i in range(len(a) - 1):
        for j in range(i, len(a)):
            val = a[i]- a[j]
            if val > 1:
                tmp.push(val)
            elif val == 1:
                return 1
        
        
    if tmp.peek():
        return tmp.peek()
    return 0
