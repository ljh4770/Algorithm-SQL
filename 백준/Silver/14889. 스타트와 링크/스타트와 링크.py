def calc_team_stats(team) -> int:
    global n, stats
    team_stats = 0
    for i in range(0, n // 2, 1):
        for j in range(i + 1, n // 2):
            team_stats += stats[team[i]][team[j]]
            team_stats += stats[team[j]][team[i]]
    return team_stats

def tracking(k, prev):
    global n, stats, min_diff
    if k == n // 2:
        link = [i for i in range(n) if visited[i] == False]
        start = [i for i in range(n) if visited[i] == True]

        diff = abs(calc_team_stats(start) - calc_team_stats(link))
        min_diff = min(min_diff, diff)
        
        return None

    for i in range(prev, n, 1):
        if visited[i] == True:
            continue

        visited[i] = True
        tracking(k + 1, i + 1)
        visited[i] = False

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    stats = [list(map(int, input().split(' '))) for _ in range(n)]
    min_diff = float('inf')
    visited = [False] * n

    tracking(0, 0)
    print(min_diff)