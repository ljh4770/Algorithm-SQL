from typing import Dict

class Node:
    def __init__(self, key: str):
        self.key: str = key
        self.child: Dict[str, 'Node'] = dict()

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, items):
        cur = self.head
        
        for word in items:
            if word not in cur.child:
                cur.child[word] = Node(word)
            cur = cur.child[word]
    
    def show(self):
        stack = []
        for _, node in sorted(self.head.child.items(), reverse=True):
            stack.append((0, node))
        
        while stack:
            d, cur = stack.pop()

            print('--' * d + cur.key)

            for _, nxt in sorted(cur.child.items(), reverse=True):
                stack.append((d + 1, nxt))


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n = int(input()) # n : [1, 1000]
    
    trie = Trie()
    for _ in range(n):
        # [(k, [string])]
        tmp = input().rstrip().split(' ')
        trie.insert(tmp[1:])
    
    trie.show()