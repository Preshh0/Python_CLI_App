#App Skeleton
import argparse
from search import breadth_first
from search import depth_first
from search import binary

def main():
    #arg parser
    parser = argparse.ArgumentParser(description="Search for word in file.")

    #word
    parser.add_argument("-w", "--word", required=True, help="Word to be searched for")
    
    #file
    parser.add_argument("-f", "--file", required=True, help="Path to file that needs to be searched.")

    #algorithm
    parser.add_argument("-sa", 
    "--search-algorithm", 
    choices=["binary-search", "depth-first-search", "breadth-first-search"], 
    required=True, 
    help="The algorithm to be used to search the file."
)

    #order
    parser.add_argument("-o", 
    "--order", 
    choices=["pre-order", "post-order", "in-order", "level-order"], 
    required=True, 
    help="The order in which to traverse the tree."
)

    #all args
    args = parser.parse_args()

    #Routes for the algorithms

    #depth first search (can use the pre, post an in order.)
    if args.search_algorithm == "depth-first-search":
        depth_first.search(args)
        return

    #breadth first search (It's traversal is synonymous to level-order. It checks all the node on a particular level from left to right before moving on to the next level.)
    if args.search_algorithm == "breadth-first-search":
        breadth_first.search(args)
        return

    # #binary search (It's left sub tree is lesser than the root and the right sub tree only contains values greater than it's root node's data. It also helps us avoid searching for our data in nodes we know the data doesn't exist; it results in a fast and efficient search.)
    if args.search_algorithm == "binary-search":
        binary.search(args)
        return

    print(args)
    print(args.search_algorithm) 
    
if __name__ == "__main__":
    main()

