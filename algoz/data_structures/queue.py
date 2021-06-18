#Queue works with FIFO. Similar to a line at a restaurant. First come, first served.
from collections import deque #deque is a double ended queue

class Queue:
    def __init__(self):
        self.nodes = deque()


    def is_empty(self,nodes):
        return len(nodes) == 0
#this adds.
    def enqueue(self, node):
        self.nodes.append(node)
#this removes and the return statement is to print out the value that was removed
    def dequeue(self):
        if not self.is_empty(self.nodes):
            return self.nodes.popleft()
#return the first item in the queue
    def peek(self):
        if not self.is_empty(self.nodes):
            return self.nodes[0]
#returns the length of the queue        
    def get_len(self):
        return len(self.nodes)
#prints out the contents of the queue
    def print_queue(self):
        print(self.nodes)