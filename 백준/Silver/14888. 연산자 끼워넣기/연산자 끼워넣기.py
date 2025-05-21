from collections import deque
from typing import Callable, List

def tracking() -> None:
    global n, nums
    if len(nums) == 0:
        global min_, max_, result
        min_ = min(min_, result)
        max_ = max(max_, result)
        return None
    
    global ops
    for i, op in enumerate(ops):
        if op == 0:
            continue
        num = nums.popleft()
        ops[i] -= 1
        prev = result
        if i == 0: # +
            result += num
            tracking()
        elif i == 1: # -
            result -= num
            tracking()
        elif i == 2: # *
            result *= num
            tracking()
        else: # /
            result = int(result / num)
            tracking()
        nums.appendleft(num)
        ops[i] += 1
        result = prev

if __name__ == '__main__':
    import sys
    input:Callable = sys.stdin.readline

    n:int = int(input())
    nums:deque[int] = deque(map(int, input().split(' ')))
    ops:List[int] = list(map(int, input().split(' ')))

    result:int = nums.popleft()
    min_:int = 10 ** 9 + 1
    max_:int = -1 * (10 ** 9 + 1)
    tracking()
    print(max_)
    print(min_)