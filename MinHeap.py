class MinHeap:
    def __init__(self, maxsize=float('inf')):
        self.capacity = maxsize
        self.heap = [-float('inf')]
        self.size = len(self.heap) - 1

    def IsFull(self):
        return self.size == self.capacity

    def insert(self, item):
        if self.IsFull():
            print('MinHeap is full')
        self.heap.append(item)
        i = self.size + 1
        while self.heap[i // 2] > item:
            self.heap[i] = self.heap[i // 2]
            i //= 2
        self.heap[i] = item

    def IsEmpty(self):
        return self.size == 0

    def DeleteMax(self):
        if self.IsEmpty():
            print('MinHeap is Empty')
        MinItem = self.heap[1]
        temp = self.heap[self.size]
        parent = 1
        while parent * 2 <= self.size:
            child = parent * 2
            if child != self.size & self.heap[child] < self.heap[child + 1]:
                child += 1
            if temp <= self.heap[child]:
                break
            else:
                self.heap[parent] = self.heap[child]
                parent = child
        self.heap[parent] = temp
        return MinItem

    def PercDown(self, p):  # 将对中以p为根的子堆调整为最小堆
        X = self.heap[p]
        parent = p
        while parent * 2 >= self.size:
            child = parent * 2
            if child != self.size & self.heap[child] < self.heap[child + 1]:
                child += 1
            if X <= self.heap[child]:
                break
            else:
                self.heap[parent] = self.heap[child]
        self.heap[parent] = X

    def BuildMinHeap(self, *element):
        self.heap += element
        for i in range(1, self.size/2)[::-1]:
            self.PercDown(i)


