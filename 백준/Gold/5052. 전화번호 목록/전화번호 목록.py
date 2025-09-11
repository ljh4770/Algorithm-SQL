import sys; input = sys.stdin.readline


class Node:
    def __init__(self, key, end_flag=False):
        self.key = key
        self.end_flag = end_flag
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head

        for char in string:
            # Insertion
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        
        # # Current input string argument is prefix.
        if cur.children:
            return False

        return True

def solve():
    n = int(input())
    numbers = [input().rstrip() for _ in range(n)]
    numbers.sort(reverse=True) # Longest string first

    trie = Trie()
    for num in numbers:
        if not trie.insert(num):
            print('NO')
            break
    else:
        print('YES')

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        solve()