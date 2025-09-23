"""
n x n Grid Map
m Trees (position can overlap)
k years simulation

Inputs
- n : [1, 10]
- m : [1, n ** 2]
- k : [1, 1000]

- A - n x n matrix with nutrient information
- A[r][c] : [1, 100]
- initial age of each tree : [1, 10]

1. Spring
- If nutrients is gte age of tree -> increase age a year
- Else -> die
- Overlap -> Youngest tree first

2. Summer
- Process dead trees
- Add nutrient to the cell with value, (age of dead tree // 2)

3. Autumn
- Reproduce(Propagation)
- If age of tree is multiple of 5 -> Create 8 tree with age 1 to adjacent cells
- Ignore for OOB cells (do not create)

4. Winter
- Add nutrients with constant value, A[r][c]

Answer
- print the number of survived trees after k years
"""

from collections import deque
from typing import Dict, List, Tuple

class Simulator:
    def __init__(
            self,
            n: int,
            nutrients: List[List[int]],
            trees: List[Tuple[int, int, int]]
    ):
        self.n: int = n
        self.map_info: List[List[int]] = nutrients
        self.cur_map: List[List[int]] = [[5] * n for _ in range(n)]
        
        self.dead_trees: List[Tuple[int, int, int]] = []
        self.survive_trees: Dict[int, deque[int]] = {
            i: deque() for i in range(n * n)
        }

        for x, y, age in trees:
            key = (x - 1) * self.n + (y - 1)
            self.survive_trees[key].append(age)

    def spring(self):
        for key, ages in self.survive_trees.items():
            if not ages:
                continue

            x, y = divmod(key, self.n)
            survived = deque()
            dead_sum = 0
            while ages:
                age = ages.popleft()
                if self.cur_map[x][y] >= age:
                    self.cur_map[x][y] -= age
                    survived.append(age + 1)
                else:
                    dead_sum += age // 2
                    for remain_tree_age in ages:
                        dead_sum += remain_tree_age // 2
                    break
            self.survive_trees[key] = survived
            self.dead_trees.append((x, y, dead_sum))
    
    def summer(self):
        for x, y, dead_sum in self.dead_trees:
            self.cur_map[x][y] += dead_sum  
        self.dead_trees = []
    
    def autumn(self):
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, 1), (1, -1), (-1, -1)
        ]
        for key, ages in self.survive_trees.items():
            if not ages:
                continue

            x, y = divmod(key, self.n)

            for age in ages:
                if age % 5 != 0:
                    continue

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < self.n and 0 <= ny < self.n):
                        continue

                    self.survive_trees[nx * self.n + ny].appendleft(1)

    def winter(self):
        for x in range(self.n):
            for y in range(self.n):
                self.cur_map[x][y] += self.map_info[x][y]
    
    def get_answer(self):
        cnt = 0
        for ages in self.survive_trees.values():
            cnt += len(ages)

        return cnt

if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n, m, k = map(int, input().split())
    nutrients = [[*map(int, input().split())] for _ in range(n)]
    trees = [tuple(map(int, input().split())) for _ in range(m)] # (x, y, age)

    sim = Simulator(n, nutrients, trees)

    for _ in range(k):
        sim.spring()
        sim.summer()
        sim.autumn()
        sim.winter()
    
    print(sim.get_answer())