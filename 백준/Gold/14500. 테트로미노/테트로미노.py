# T미노 제외 탐색
def dfs(x, y, tmp, cnt):
    global n, m, paper
    global visited, directions
    global answer

    if cnt == 4:
        answer = max(answer, tmp)
        return None
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < n and 0 <= ny < m):
            continue

        if visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx, ny, tmp + paper[nx][ny], cnt + 1)
            visited[nx][ny] = False

def search_t(x, y):
    global n, m, paper
    global directions
    global answer

    tmp = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < n and 0 <= ny < m):
            continue
        tmp.append(paper[nx][ny])

    if len(tmp) == 4:
        tmp.sort(reverse=True)
        tmp.pop()
        answer = max(answer, sum(tmp) + paper[x][y])
    elif len(tmp) == 3:
        answer = max(answer, sum(tmp) + paper[x][y])
    
    return None

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    paper = [list(map(int, input().split(' '))) for _ in range(n)]

    visited = [[False] * m for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = 0

    for x in range(n):
        for y in range(m):
            visited[x][y] = True
            dfs(x, y, paper[x][y], 1)
            search_t(x, y)
            visited[x][y] = False

    print(answer)