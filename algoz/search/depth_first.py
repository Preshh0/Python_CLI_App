from algoz.data_structures.binary_tree import BinaryTree
#the order checks in the root, left right order according to family
def pre_order_search(target, root):
    if root:

        if root.data == target:
            return True

        if pre_order_search(target, root.left):
            return True

        if pre_order_search(target, root.right):
            return True

    return False
            
def search(args):
    bt = BinaryTree()

    print("Building tree...")
    bt.create_from_file(args.file)
    print("Tree built!")

    if args.order == "pre-order":
        print("Searching tree...")

        target = args.word

        if pre_order_search(target, bt.root):
            print("Word Found!")
        else:
            print("Word not found :(")

        