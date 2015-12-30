class BinaryTree:
    def __init__(self):
        self.tree = EmptyNode()

    def __repr__(self):
        return repr(self.tree)

    def lookup(self, value):
        return self.tree.lookup(value)

    def insert(self, value):
        self.tree = self.tree.insert(value)


class EmptyNode:
    def __repr__(self):
        return '*'

    def lookup(self, value):
        return False

    def insert(self, value):
        return BinaryNode(self, value, self)


class BinaryNode:

    def __init__(self, left, value, right):
        self.data, self.left, self.right = value, left, right

    def lookup(self, value):
        path = []
        if self.data == value:
            return self.data
        elif self.data > value:
            print(self.data, end='->')  # print the root path
            return self.left.lookup(value)
        else:
            print(self.data, end='->')  # print the root path
            return self.right.lookup(value)

    def insert(self, value):
        if self.data > value:
            self.left = self.left.insert(value)
        elif self.data < value:
            self.right = self.right.insert(value)
        elif self.data == value:
            print('Data already exist')
        return self

    def __repr__(self):
        return '(%s, %s, %s)' % (repr(self.left), repr(self.data), repr(self.right))


if __name__ == '__main__':
    y = BinaryTree()
    print(y)
    for i in [3, 1, 9, 2, 7]:
        y.insert(i)
        print(y)

    print(y.lookup(7))  # test lookup