def expand():
    global r, c
    global room, machine

    room_next = [[0] * c for _ in range(r)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x in range(r):
        for y in range(c):
            if room[x][y] in [-1, 0]:
                continue
            dust = room[x][y]
            dust_expanding = dust // 5
            expand_cnt = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < r and 0 <= ny < c) or room[nx][ny] == -1:
                    continue
                room_next[nx][ny] += dust_expanding
                expand_cnt += 1
            room_next[x][y] += dust - dust_expanding * expand_cnt
    for x in machine:
        room_next[x][0] = -1
    
    return room_next

def rotate():
    global r, c
    global room, machine

    # Rotate Upper Area
    upper = machine[0]
    for x in range(upper - 1, 0, -1):
        room[x][0] = room[x - 1][0]
    for y in range(0, c - 1, 1):
        room[0][y] = room[0][y + 1]
    for x in range(0, upper, 1):
        room[x][c - 1] = room[x + 1][c - 1]
    for y in range(c - 1, 1, -1):
        room[upper][y] = room[upper][y - 1]
    room[upper][1] = 0

    # Rotate Lower Area
    lower = machine[1]
    for x in range(lower + 1, r - 1, 1):
        room[x][0] = room[x + 1][0]
    for y in range(0, c - 1, 1):
        room[r - 1][y] = room[r - 1][y + 1]
    for x in range(r - 1, lower , -1):
        room[x][c - 1] = room[x - 1][c - 1]
    for y in range(c - 1, 1, -1):
        room[lower][y] = room[lower][y - 1]
    room[lower][1] = 0

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    r, c, t = map(int, input().split(' '))
    room = [[*map(int, input().split(' '))] for _ in range(r)]
    machine = []

    for x in range(r):
        if room[x][0] == -1:
            machine.append(x)
            machine.append(x + 1)
            break

    for _ in range(t):
        room = expand()
        rotate()

    dust_amt = 0
    for x in range(r):
        for y in range(c):
            if room[x][y] > 0:
                dust_amt += room[x][y]
    print(dust_amt)