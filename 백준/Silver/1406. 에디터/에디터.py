class Editor:
    def __init__(self, contents):
        self.left = []
        for c in contents:
            self.left.append(c)
        self.right = []

    def __str__(self):
        return ''.join(self.left) + ''.join(reversed(self.right))

    def L(self):
        if self.left:
            item = self.left.pop()
            self.right.append(item)

    def D(self):
        if self.right:
            item = self.right.pop()
            self.left.append(item)

    def B(self):
        if self.left:
            self.left.pop()

    def P(self, X):
        self.left.append(X)

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    contents = input().strip()
    M = int(input())
    queries = [input().strip() for _ in range(M)]

    editor = Editor(contents)

    for query in queries:
        query = query.split(' ')

        if query[0] == 'L':
            editor.L()
        if query[0] == 'D':
            editor.D()
        if query[0] == 'B':
            editor.B()
        if query[0] == 'P':
            editor.P(query[1])

    print(editor)
