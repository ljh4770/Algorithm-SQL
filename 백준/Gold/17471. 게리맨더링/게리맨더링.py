import sys; sys.setrecursionlimit(10 ** 4)
from collections import deque

def check():
    '''
    BFS to validate the graph
    '''
    q = deque()
    visited = [False] * (n + 1)
    
    # Enqueue seed node of each region in the queue
    flag0, flag1 = False, False
    for i, r in  enumerate(region[1:], start=1):
        if flag0 == False and r == False:
            q.append(i)
            visited[i] = True
            flag0 = True
        elif flag1 == False and r == True:
            q.append(i)
            visited[i] = True
            flag1 = True
        if flag0 and flag1:
            break
    # If one of region is not enqueued -> invalid
    if not (flag0 and flag1):
        return False

    while q: # BFS
        cur = q.popleft()

        for nxt in graph[cur]:
            if visited[nxt] == False and region[nxt] == region[cur]:
                q.append(nxt)
                visited[nxt] = True
    
    # If node not visited exist -> invalid
    if False in visited[1:]:
        return False

    return True


def get_diff():
    '''
    return difference bwetween populations from each region 
    '''
    sum_ = 0
    for i, r in enumerate(region[1:], start=1):
        if r == False:
            sum_ += populations[i]
        else:
            sum_ -= populations[i]

    return abs(sum_)


def tracking(idx):
    global answer

    if check() == True: # If the graph set is valid
        answer = min(answer, get_diff())

    for i in range(idx + 1, n + 1, 1):
        region[i] = True
        tracking(i)
        region[i] = False


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input()) # n : [2, 10]
    # [population, ...] : [1, 100]
    populations = [0] + [*map(int, input().split())]

    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        # [num_edage, adjacent nodes,...]
        _, *adjacent = map(int, input().split(' '))
        graph[i] = adjacent
    
    # False -> 0 region / True -> 1 region
    region = [False] * (n + 1)
    answer = float('inf') # minimize task
    tracking(0)

    if answer == float('inf'):
        print(-1)
    else:
        print(answer)