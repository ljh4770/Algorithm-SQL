from typing import List, Tuple

class Simulation:
    def __init__(self, r: int, c: int, sharks: List[Tuple[int]]):
        self.r = r
        self.c = c

        self.pos = -1 # Current position of the fisherman
        self.score = 0 # Sum of sizes of caught sharks

        self.directions = {
            1: (-1, 0),  # Up
            2: (1, 0),   # Down
            3: (0, 1),   # Right
            4: (0, -1)   # Left
        }

        self.grid = [[0] * c for _ in range(r)]
        self.shark_info = dict() # Information about sharks in the grid
        # key is size of the shark
        # value is a tuple (row, column, speed, direction)
        
        for r, c, s, d, z in sharks:
            # Convert to 0-based index
            self.grid[r - 1][c - 1] = z
            self.shark_info[z] = (r - 1, c - 1, s, d)
        
        self.cycle_r = 2 * (r - 1) if r > 1 else 1
        self.cycle_c = 2 * (c - 1) if c > 1 else 1

    def run(self):
        while self.pos < self.c - 1:
            self.move_and_catch()
            self.move_sharks()

    def move_and_catch(self):
        # Move the fisherman to the next column and catch sharks
        self.pos += 1
        
        for r in range(self.r):
            if self.grid[r][self.pos] > 0:
                size = self.grid[r][self.pos]
                self.grid[r][self.pos] = 0
                self.score += size
                del self.shark_info[size]
                break

    def move_sharks(self):
        next_grid = [[0] * self.c for _ in range(self.r)]
        next_info = dict()

        for size, (r, c, s, d) in self.shark_info.items():
            if d in (1, 2):
                s = s % (2 * (self.r - 1))
            else:
                s = s % (2 * (self.c - 1))

            nr, nc, nd = self._next_position(r, c, s, d)
            if next_grid[nr][nc] > 0:
                prev_size = next_grid[nr][nc]
                if size > prev_size:
                    next_grid[nr][nc] = size
                    next_info[size] = (nr, nc, s, nd)
                    del next_info[prev_size]
            else:
                next_grid[nr][nc] = size
                next_info[size] = (nr, nc, s, nd)
        
        self.grid = next_grid
        self.shark_info = next_info
   
    def _next_position(self, r: int, c: int, s: int, d: int) -> Tuple[int, int, int]:
        if d == 1 or d == 2:  # i
            cycle = self.r * 2 - 2
            if d == 1:
                s += 2 * (self.r - 1) - r
            else:
                s += r

            s %= cycle
            if s >= self.r:
                return (2 * self.r - 2 - s, c, 1)
            return (s, c, 2)

        else:  # j
            cycle = self.c * 2 - 2
            if d == 4:
                s += 2 * (self.c - 1) - c
            else:
                s += c

            s %= cycle
            if s >= self.c:
                return (r, 2 * self.c - 2 - s, 4)
            return (r, s, 3)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    # map with size, r x c
    # m: number of sharks
    r, c, m = map(int, input().split(' '))
    if m == 0:
        print(0)
        exit(0)

    # (r, c, s, d, z) == (pos_r, pos_c, speed, direction, size)
    # 1-based r and c
    # d: 1-Up, 2-Down, 3-Right, 4-Left
    # z: size of the shark is unique
    sharks = [tuple(map(int, input().split(' '))) for _ in range(m)]

    simulation = Simulation(r, c, sharks)
    simulation.run()
    print(simulation.score)