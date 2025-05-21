class KeyLogger():
    def __init__(self):
        self.left = []
        self.right = []

    def __str__(self):
        left = ''.join(self.left)
        right = ''.join(reversed(self.right))
        return left + right

    def log(self, X):
        self.left.append(X)

    def move_left(self):
        if self.left:
            item = self.left.pop()
            self.right.append(item)

    def move_right(self):
        if self.right:
            item = self.right.pop()
            self.left.append(item)
        
    def erase(self):
        if self.left:
            self.left.pop()


if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    T = int(input())
    data = [input().strip() for _ in range(T)]

    for log in data:
        logger = KeyLogger()
        for c in log:
            if c == '<':
                logger.move_left()
            elif c == '>':
                logger.move_right()
            elif c == '-':
                logger.erase()
            else:
                logger.log(c)
        print(logger)

