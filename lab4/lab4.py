class Tree:
    def __init__(self, item=None):
        self.left = None
        self.right = None
        self.item = item

    def insert(self, item):
        if not self.item:
            self.item = item
            return

        if self.item == item:
            return

        if item < self.item:
            if self.left:
                self.left.insert(item)
                return
            self.left = Tree(item)
            return

        if self.right:
            self.right.insert(item)
            return
        self.right = Tree(item)

    def delete(self, item):
        if item < self.item:
            if self.left:
                self.left = self.left.delete(item)
            return self
        if item > self.item:
            if self.right:
                self.right = self.right.delete(item)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.item = min_larger_node.item
        self.right = self.right.delete(min_larger_node.item)
        return self

    def exists(self, item):
        if item == self.item:
            return True

        if item < self.item:
            if self.left == None:
                return False
            return self.left.exists(item)

        if self.right == None:
            return False
        return self.right.exists(item)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.item)
        if self.right:
            self.right.printTree()

tree = Tree(1)
tree.insert(63)
tree.insert(222)
tree.insert(4)
tree.insert(500)
tree.delete(222)

print(tree.exists(500))
print(tree.exists(502))

tree.printTree()