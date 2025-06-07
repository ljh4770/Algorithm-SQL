from collections import deque

def bfs(x, y, group):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0

    while q:
        x, y = q.popleft()
        zero_group[x][y] = group # Assign the group number to the cell
        cnt += 1 # count the size of the chunk, movable cells

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # continue if out of bounds
            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if visited[nx][ny] == False and map_[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))

    return cnt

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    map_ = [[*map(int, input().rstrip())] for _ in range(n)]
    group_cnt = dict() # chunk size of each group
    zero_group = [[0] * m for _ in range(n)] # group number of each blank cell
    
    # Count cell with walls
    visited = [[False] * m for _ in range(n)]
    group = 0
    for x in range(n):
        for y in range(m):
            # If the cell is a movable chunk
            if map_[x][y] == 0 and visited[x][y] == False:
                cnt = bfs(x, y, group) # Count the movable chunk size
                group_cnt[group] = cnt # Store the size of the chunk
                group += 1

    # Count cell from a wall
    wall_cnt = [[0] * m for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x in range(n):
        for y in range(m):
            if map_[x][y] == 1:
                group_set = set()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m):
                        continue

                    if map_[nx][ny] == 0:
                         # Add the group number of the adjacent zero cell
                        group_set.add(zero_group[nx][ny])
                
                cnt = 0
                for g in group_set:
                    cnt += group_cnt[g]

                wall_cnt[x][y] = (cnt + 1) % 10

    for row in wall_cnt:
        print(*row, sep='')