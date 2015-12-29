from MinHeap import MinHeap

class HuffmanTreeNode:
    def __init__(self, weight, left, right):
        self.weight = weight
        self.left = left
        self.right = right


class HuffmanTree:
    def __init__(self, *elements):
        self.tree = MinHeap.BuildMinHeap(self, elements)




