from typing import Dict, List, Tuple, Set, TypeAlias


Coords: TypeAlias = Set[Tuple[int, int]]

class Clouds:
    COST: int = 2
    DITECTIONS: Dict[int, Tuple[int, int]] = {
        1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
        5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)
    }

    def __init__(self, n: int):
        self.n = n
        self.clouds_pos: Coords = {
            (n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)
        }

    def move_and_rain(self, target: List[List[int]], d: int, s: int) -> Coords:
        dx, dy = Clouds.DITECTIONS[d]
        self.clouds_pos: Coords = {
            (
                (x + s * dx) % self.n,
                (y + s * dy) % self.n
            ) for x, y in self.clouds_pos
        }

        for x, y in self.clouds_pos:
            target[x][y] += 1

        return self.clouds_pos

    def update_gen(self, target: List[List[int]]):
        next_gen: Coords = set()
        for x in range(self.n):
            for y in range(self.n):
                if (x, y) in self.clouds_pos:
                    continue

                if target[x][y] < self.COST:
                    continue

                target[x][y] -= self.COST
                next_gen.add((x, y))
        self.clouds_pos = next_gen


class Shark:
    DITECTIONS: List[Tuple[int, int]] = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    def __init__(self, n: int):
        self.n = n

    def magic(self, target: List[List[int]], coords: Coords):
        for x, y in coords:
            for dx, dy in Shark.DITECTIONS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < self.n and 0 <= ny < self.n):
                    continue

                if target[nx][ny] > 0:
                    target[x][y] += 1


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    N, M = map(int, input().split())
    grid = [[*map(int, input().split())] for _ in range(N)]
    commands = [tuple(map(int, input().split())) for _ in range(M)]

    shark = Shark(N)
    clouds = Clouds(N)
    for d, s in commands:
        rained_pos = clouds.move_and_rain(grid, d, s)
        shark.magic(grid, rained_pos)
        clouds.update_gen(grid)

    print(sum(sum(row) for row in grid))
