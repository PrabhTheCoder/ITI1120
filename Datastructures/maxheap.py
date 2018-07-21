class MaxHeap:
    def __init__(self,  items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)
    def push(self, data):
        """(MaxHeap, Object) -> None
            Pushes data into the heap.
        """
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
        
    def peek(self):
        """(MaxHeap) -> Object
            Returns the maximum item in the heap
        """
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return False
    def pop(self):
        """(MaxHeap) -> Object
            Returns and removes the maximum object in the heap.
        """
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1) #Swaps last element and max to allow popping in const time
            maximum = self.heap.pop()
            self.__maxHeapify(1) #Puts everything back where it belongs
        elif len(self.heap) == 2:
            maximum = self.heap.pop()
        else:
            maximum = False
        return maximum
    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def __floatUp(self, index):
        parent = index // 2
        #reached top of heap so just return
        if index <= 1:
            return
        #if child is greater than parent, swap them and perform same checks on the parent of the parent.
        elif self.heap[index] > self.heap[parent]: 
            self.__swap(index, parent)
            self.__floatUp(parent)
    def __maxHeapify(self, index):
        left = index * 2 #left child
        right = index * 2 + 1 #right child
        largest = index #initially assumes index is the largest

        #if left child exists, and the current largest is smaller than the left
        #child set the largest as the left childs index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        #if the right child exists, and the current largest is  smaller than
        #the right child set the largest as the right childs index.
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            #if the largest isnt the current number, swap places with the largest
            #and then perform same operations on the index the current item was
            #moved to.
            self.__swap(index, largest)
            self.__maxHeapify(largest)
