import sys
from typing import List
from collections import deque
input = sys.stdin.readline

class FourGears():
    def __init__(self, gears: List[deque[int]]):
        self.gears = gears
    
    def _clock_wise(self, i) -> None:
        item = self.gears[i].pop()
        self.gears[i].appendleft(item)

    def _counter_clock_wise(self, i) -> None:
        item = self.gears[i].popleft()
        self.gears[i].append(item)

    def rotate(self, i, d, check_left = True, check_right = True) -> None:
        left = self.gears[i][6]
        right = self.gears[i][2] 
        if check_left == True and i != 0:
            if self.gears[i - 1][2] != left:
                self.rotate(i - 1, -d, check_right = False)
        if check_right == True and i != 3:
            if self.gears[i + 1][6] != right:
                self.rotate(i + 1, -d, check_left = False)

        if d == 1:
            self._clock_wise(i)
        elif d == -1:
            self._counter_clock_wise(i)

    def scoring(self) -> int:
        score = 0
        for i in range(4):
            if self.gears[i][0] == 1:
                score += 2 ** i
        return score

if __name__ == '__main__':
    gears = [deque(map(int, list(input().rstrip()))) for _ in range(4)]
    k = int(input())
    operations = [tuple(map(int, input().split(' '))) for _ in range(k)]

    my_gears = FourGears(gears)
    for i, d in operations:
        my_gears.rotate(i - 1, d)
    
    score = my_gears.scoring()
    print(score)