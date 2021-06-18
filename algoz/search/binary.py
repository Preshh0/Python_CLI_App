from data_structures.binary_tree import BinaryTree

def binary_search(target, root):
    if root:

        if int(root.data) == int(target):
            return True
        
        if int(root.data) < int(target):
            if binary_search(target, root.right):
                return True
        
        if binary_search(target, root.left):
            return True
             
    return False

def search(args):
    bst = BinaryTree() #a binary search tree is a type of binary tree.

    print("Building tree...")
    bst.create_bst_from_file(args.file) #this line converts a normal binary tree into a search tree
    print("Tree Built!")

    print("Searching Tree...")

    target = args.word

    if binary_search(target, bst.root):
        print("word found!")
        return
    else:
        print("word not found :(")
        return