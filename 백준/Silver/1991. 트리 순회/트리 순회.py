from __future__ import annotations
import sys
from typing import List

class Node:
    def __init__(self, value:str):
        self.value:str = value
        self.parent:Node = None
        self.left:Node = None
        self.right:Node = None
    
    def add_left(self, node:Node):
        self.left = node
        node.__add_parent(self)
    
    def add_right(self, node:Node):
        self.right = node
        node.__add_parent(self)

    def __add_parent(self, node:Node):
        self.parent = node
    
    def preorder_traversal(self):
        print(self.value, end='')
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value, end='')
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value, end='')

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    infos = [input().rstrip().split(' ') for _ in range(n)]
    nodes:List[Node] = []

    for c, l, r in infos:
        for node in nodes: # Find current node
            if node.value == c:
                cur = node
                break
        else: # Create node if not exist
            cur = Node(c)
            nodes.append(cur)
        if l != '.': # add left child
            for node in nodes:
                if node.value == l:
                    cur.add_left(node)
                    break
            else:
                node = Node(l)
                nodes.append(node)
                cur.add_left(node)
        if r != '.': # add right child
            for node in nodes:
                if node.value == r:
                    cur.add_right(node)
                    break
            else:
                node = Node(r)
                nodes.append(node)
                cur.add_right(node)
    nodes[0].preorder_traversal()
    print()
    nodes[0].inorder_traversal()
    print()
    nodes[0].postorder_traversal()
    print()