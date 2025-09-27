def solve(n, order, favs):
    seats = [[0] * n for _ in range(n)]
    neighbor = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def find(student, fav):
        nonlocal n, seats
        nonlocal neighbor

        fav_score = 10
        blk_score = 1
        
        max_score = -1
        max_x, max_y = -1, -1
        for x in range(n):
            for y in range(n):
                # occupied seat
                if seats[x][y] != 0:
                    continue
                # check neighbor seats and scoring
                cur_score = 0
                for dx, dy in neighbor:
                    nx, ny = x + dx, y + dy
                    # OOB
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    
                    if seats[nx][ny] in fav:
                        cur_score += fav_score
                    elif seats[nx][ny] == 0:
                        cur_score += blk_score

                # update max score and coord of seat
                if cur_score > max_score:
                    max_score = cur_score
                    max_x, max_y = x, y

        # assign to seats
        seats[max_x][max_y] = student
    
    def clac_happiness(sx, sy, fav):
        nonlocal neighbor

        fav_cnt = 0
        for dx, dy in neighbor:
            nx, ny = sx + dx, sy + dy

            # OOB
            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if seats[nx][ny] in fav:
                fav_cnt += 1

        return 10 ** (fav_cnt - 1) if fav_cnt > 0 else 0

    # assign seat
    for student, fav in zip(order, favs):
        find(student, fav)
    
    # calculate total happiness
    total_happiness = 0
    for x in range(n):
        for y in range(n):
            student = seats[x][y]
            fav_idx = order.index(student)
            fav = favs[fav_idx]
            total_happiness += clac_happiness(x, y, fav)

    return total_happiness


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n = int(input())
    stream = [[*map(int, input().split())] for _ in range(n ** 2)]
    order = []
    favs = []
    for line in stream:
        order.append(line[0])
        favs.append(line[1:])

    answer = solve(n, order, favs)
    print(answer)