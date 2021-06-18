from data_structures.node import Node
from data_structures.queue import Queue

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
    
    def bst_insert_recursive(self, data, root):

        if int(data) < int(root.data):
            if root.left is None:
                root.left = Node(data)
            else:
                self.bst_insert_recursive(data, root.left)
        
        if int(data) > int(root.data):
            if root.right is None:
                root.right = Node(data)
            else:
                self.bst_insert_recursive(data, root.right)


    def bst_insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.bst_insert_recursive(data, self.root)

#used for converting the contents of .txt file to a tree structure so it can be traversed using a tree traversal algorithm. 
    def create_from_file(self, path):
        with open(path, "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                if stripped_line is not "":
                    words = stripped_line.split()
                    for word in words:
                        self.level_order_insert(word)

    def create_bst_from_file(self, path):
        with open(path, "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                if stripped_line is not " ":
                    words = stripped_line.split()
                    for word in words:
                        self.bst_insert(word)

    def in_order_print(self, root):
        if root:
            self.in_order_print(root.left)
            print(root.data)
            self.in_order_print(root.right)

#an in_order function can help confirm if a binary search tree has been implemented correctly