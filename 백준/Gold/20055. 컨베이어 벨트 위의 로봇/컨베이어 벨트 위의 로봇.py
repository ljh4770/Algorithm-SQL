from typing import List
from collections import deque

class RobotSimulator:
    def __init__(self, cells: List[int], n: int, k: int):
        self.cells: deque[int] = deque(cells)
        self.robot_pos: deque[bool] = deque([False] * (len(cells) // 2))
        self.step_cnt = 1
        self.n = n
        self.k = k

    def rotate_belt1(self):
        # rotate belt with robot
        self.cells.rotate(1)
        self.robot_pos.rotate(1)

        # unmount robot if exist on last cell
        if self.robot_pos[-1]:
            self.robot_pos[-1] = False

    def move_robot2(self):
        # There not exist robot on the last cell

        # move robot and decrease the durabilit
        for pos in range(self.n - 2, -1, -1):
            if self.robot_pos[pos]:
                # remained durability & empty cell
                if self.cells[pos + 1] > 0 and not self.robot_pos[pos + 1]:
                    self.robot_pos[pos] = False
                    self.robot_pos[pos + 1] = True
                    self.cells[pos + 1] -= 1
        # unmount robot if exist on last cell
        if self.robot_pos[-1]:
            self.robot_pos[-1] = False

    def mount_robot3(self):
        if self.cells[0] > 0 and not self.robot_pos[0]:
            self.robot_pos[0] = True
            self.cells[0] -= 1

    def finish_check4(self):
        cnt = 0
        for d in self.cells:
            if d <= 0:
                cnt += 1
        
        if cnt >= self.k:
            return True
        
        self.step_cnt += 1
        return False


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    # n : [2, 100], k : [1, 2n]
    # cells_i : [1, 1000]
    n, k = map(int, input().split())
    cells = [*map(int, input().split())]

    sim = RobotSimulator(cells, n, k)

    while True:
        sim.rotate_belt1()
        sim.move_robot2()
        sim.mount_robot3()
        if sim.finish_check4():
            break
    
    print(sim.step_cnt)