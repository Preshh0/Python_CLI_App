from algoz.data_structures.node import Node
from algoz.data_structures.queue import Queue

class BinaryTree: #a binary tree is a tree whose nodes are not more than two children(one left, one right). Leaf node have no children. A binary search tree is a type of binary tree, but all binary trees are not binary search trees. 
    def __init__(self):
        self.root = None
#method used to build the binary tree
    def level_order_insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        queue = Queue()
        queue.enqueue(self.root)

        while queue.get_len():
            node = queue.dequeue()

            if not node.left:
                node.left = Node(data)
                return
            else:
                queue.enqueue(node.left)

            if not node.right:
                node.right = Node(data)
                return
            else:
                queue.enqueue(node.right)


