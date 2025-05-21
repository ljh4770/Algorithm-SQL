class Dice():
    def __init__(self, x, y):
        self.bottom = 0
        self.top = 0
        self.north = 0
        self.south = 0
        self.west = 0
        self.east = 0
        self.x, self.y = x, y

    def move(self, op, n, m) -> int:
        """
        move the dice if possible
        return bottom number after move
        return none if move is impossible
        """
        x, y = self.x, self.y
        if op == 1: # East, fix north south
            if not (0 <= y + 1 < m): # Out of map
                return None
            self.bottom, self.top, self.west, self.east = self.east, self.west, self.bottom, self.top
            self.y = y + 1
        elif op == 2: # West, fix north south
            if not (0 <= y - 1 < m): # Out of map
                return None
            self.bottom, self.top, self.west, self.east = self.west, self.east, self.top, self.bottom
            self.y = y - 1
        elif op == 3: # North, fix west east
            if not (0 <= x - 1 < n):
                return None
            self.bottom, self.top, self.north, self.south = self.north, self.south, self.top, self.bottom
            self.x = x - 1
        elif op == 4: # South, fix west east
            if not (0 <= x + 1 < n):
                return None
            self.bottom, self.top, self.north, self.south = self.south, self.north, self.bottom, self.top
            self.x = x + 1
        else:
            raise Exception(f"Unprocessable opreration: {op}")
        return self.bottom

import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split(' '))

map_ = [[*map(int, input().split(' '))] for _ in range(n)]
operations = [*map(int, input().split(' '))]

my_dice = Dice(x, y)
for op in operations:
    res = my_dice.move(op, n, m)
    
    if res != None: # moved
        x, y = my_dice.x, my_dice.y
        if map_[x][y] == 0:
            map_[x][y] = res
        else:
            my_dice.bottom = map_[x][y]
            map_[x][y] = 0
        print(my_dice.top)