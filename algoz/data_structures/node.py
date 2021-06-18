#data structuer for a node that'd be used in the binary tree module

class Node():
    def __init__(self, data):
        self.data = data #stuff stored inside node
        self.left = None #represents the left child of the node
        self.right = None #represents the right child of the node