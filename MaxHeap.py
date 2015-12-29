class MaxHeap:
    def __init__(self, maxsize):
        self.capacity = maxsize
        self.heap = [float('inf')]  # set the first element as a guard
        self.size = len(self.heap) - 1

    def IsFull(self):
        return self.size == self.capacity

    def insert(self, item):
        if self.IsFull():
            print('Max Heap is full')
        self.heap.append(item)
        i = self.size + 1
        while self.heap[i // 2] < item:  # compare with parent node if bigger then move upward
            self.heap[i] = self.heap[i // 2]
            i //= 2
        self.heap[i] = item  # find the right place and then put item in

    def IsEmpty(self):
        return self.size == 0

    def DeleteMax(self):
        if self.IsFull():
            print('Max Heal is full')
        MaxItem = self.heap[1]
        temp = self.heap[self.size]
        parent = 1
        while parent * 2 <= self.size:  # if the left child is exist
            child = parent * 2
            if child != self.size & self.heap[child] < self.heap[child + 1]:
                child += 1  # point child to the larger one
            if temp >= self.heap[child]:
                break
            else:
                self.heap[parent] = self.heap[child]
                parent = child
        self.heap[parent] = temp
        return MaxItem

    def PercDown(self, p):  # 将对中以p为根的子堆调整为最大堆
        X = self.heap[p]
        parent = p
        while parent * 2 <= self.size:
            child = parent * 2
            if child != self.size & self.heap[child] < self.heap[child + 1]:
                child += 1
            if X >= self.heap[child]:
                break
            else:
                self.heap[parent] = self.heap[child]
        self.heap[parent] = X
