from typing import List

class Node:
    def __init__(self, key: str):
        self.key = key # key by string, not char
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, line: List[str]):
        cur = self.head

        for name in line: # Iterate over directory names in the path
            if name not in cur.children:
                cur.children[name] = Node(name)
            cur = cur.children[name]

    def show(self):
        cur = self.head
        self.dfs(cur, 0) # dfs to show directory structure

    def dfs(self, cur, depth):
        for key, nxt in sorted(cur.children.items()):
            print(' ' * depth + key)
            self.dfs(nxt, depth + 1)


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n = int(input()) # n : [1, 500]
    # Directory path separated by '\', each path length <= 80
    lines = [input().rstrip().split('\\') for _ in range(n)]

    trie = Trie()
    for line in lines:
        trie.insert(line)
    
    trie.show()