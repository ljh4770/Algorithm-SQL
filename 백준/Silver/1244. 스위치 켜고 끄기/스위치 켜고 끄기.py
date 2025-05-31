from typing import List

class Switches:
    def __init__(self, status: List[int]):
        self.num_switches: int = len(status)
        self.status: List[bool] = []

        for stat in status:
            if stat == 0:
                self.status.append(False)
            elif stat == 1:
                self.status.append(True)
            else:
                raise ValueError("Switch status must be either 0 or 1.")

    def __str__(self):
        string = []
        for stat in self.status:
            if stat == True:
                string.append('1')
            else:
                string.append('0')
        
        lines = []
        for i in range(0, self.num_switches, 20):
            chunk = ' '.join(string[i:i+20])
            lines.append(chunk)

        return '\n'.join(lines)

    def toggle_multiple(self, num: int):
        '''
        Toggle the switch at position `num`
        and all multiples of it.
        '''
        multiple = num
        while multiple <= self.num_switches:
            self.status[multiple - 1] = not self.status[multiple - 1]
            multiple += num

    def toggle_symmetric(self, num: int):
        '''
        Toggle the swich at position `num`
        and all symmetric switches around it.
        '''
        base = num - 1
        self.status[base] = not self.status[base]

        for i in range(1, self.num_switches // 2 + 1, 1):
            if not (0 <= base - i and base + i < self.num_switches):
                break
            if self.status[base - i] != self.status[base + i]:
                break
            self.status[base - i] = not self.status[base - i]
            self.status[base + i] = not self.status[base + i]


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    num_switches = int(input())
    status = [*map(int, input().split(' '))]
    num_students = int(input())
    toggle_info = []
    for _ in range(num_students):
        sex, num = map(int, input().split(' '))
        toggle_info.append((sex, num))

    switches = Switches(status)

    for sex, num in toggle_info:
        if sex == 1: # Boy
            switches.toggle_multiple(num)
        elif sex == 2: # Girl
            switches.toggle_symmetric(num)
    
    print(switches)