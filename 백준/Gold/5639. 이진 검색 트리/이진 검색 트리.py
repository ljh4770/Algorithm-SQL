import sys
from collections import deque
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self, value):
        self.value = value
        self.parent:Node = None
        self.left:Node = None
        self.right:Node = None

    def add_left(self, node):
        self.left = node
        if node:
            node._add_parent(self)

    def add_right(self, node):
        self.right = node
        if node:
            node._add_parent(self)
    
    def _add_parent(self, node):
        self.parent = node

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
        

def build_tree(values:deque[int]):
    if not values:
        return None
    root = Node(values.popleft())
    tmp_left = deque()

    while values and root.value > values[0]:
        tmp_left.append(values.popleft())
    
    root.add_left(build_tree(tmp_left))
    root.add_right(build_tree(values))

    return root

if __name__ == '__main__':
    values = deque()
    for line in sys.stdin:
        values.append(int(line))
    
    root = build_tree(values)
    root.postorder_traversal()