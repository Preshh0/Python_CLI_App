#App Skeleton
import argparse


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
    choices=["pre-order", "post-order", "level-order"], 
    required=True, 
    help="The order in which to traverse the tree."
)

    #all args
    args = parser.parse_args()
    
    #Routes for the algorithms
    #depth first search
    if args.search_algorithm == "depth-first-search":
        depth_first.search(args)
        return

    #breadth first search
    if args.search_algorithm == "breadth-first-search":
        breadth_first.search(args)
        return

    #breadth first search
    if args.search_algorithm == "binary-search":
        binary.search(args)
        return

    # print(args)
    # print(args.search_algorithm) 
    
if __name__ == "__main__":
    main()
