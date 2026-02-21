from typing import Dict, List, Tuple, Set


class Shark:
    # 0: left, 1: down, 2: right, 3: up
    AFFECT_POS_RATIO: Dict[int, Set[Tuple[int, int, float]]] = {
        0: {
            (-2, 0, 0.02),
            (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),
            (0, -2, 0.05),
            (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01),
            (2, 0, 0.02)
        },
        1: {
            (-1, -1, 0.01), (-1, 1, 0.01),
            (0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02),
            (1, -1, 0.1), (1, 1, 0.1),
            (2, 0, 0.05)
        },
        2: {
            (-2, 0, 0.02),
            (-1, -1, 0.01), (-1, 0, 0.07), (-1, 1, 0.1),
            (0, 2, 0.05),
            (1, -1, 0.01), (1, 0, 0.07), (1, 1, 0.1),
            (2, 0, 0.02)
        },
        3: {
            (-2, 0, 0.05),
            (-1, -1, 0.1), (-1, 1, 0.1),
            (0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02),
            (1, -1, 0.01), (1, 1, 0.01)
        }
    }
    DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self, n: int):
        self.n = n

    def magic(self, target: List[List[int]]):
        x, y = self.n // 2, self.n // 2 # current point
        d = 0 # current direction
        s = 1 # distance from direction change

        sand_amount_total = 0
        while True:
            for _ in range(2):
                for _ in range(s):
                    dx, dy = Shark.DIRECTIONS[d]
                    x, y = x + dx, y + dy
                    if y < 0:
                        return sand_amount_total

                    sand_amount = 0 # amount of sand s.t. OOB
                    original_amount = target[x][y]
                    # distribute sand
                    for dx, dy, r in Shark.AFFECT_POS_RATIO[d]:
                        nx, ny = x + dx, y + dy
                        da = int(original_amount * r)
                        target[x][y] -= da

                        if not (0 <= nx < self.n and 0 <= ny < self.n):
                            sand_amount += da
                        else:
                            target[nx][ny] += da

                    # calc remainder (alpha)
                    dx, dy = Shark.DIRECTIONS[d]
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < self.n and 0 <= ny < self.n):
                        sand_amount += target[x][y]
                    else:
                        target[nx][ny] += target[x][y]
                    target[x][y] = 0

                    sand_amount_total += sand_amount
                d = (d + 1) % 4 # change direction
            s += 1 # add distance


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    N = int(input()) # odd number
    grid = [[*map(int, input().split())] for _ in range(N)]

    shark = Shark(N)
    print(shark.magic(grid))
