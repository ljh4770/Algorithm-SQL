from collections import deque

def topological_sort(graph, indegree, n):
    q = deque()
    # Assign Fianl materials to queue
    for i in range(1, n + 1):
        # Middle matetials with indegree 0 also assigned to resolve the relations
        if indegree[i] == 0:
            q.append(i)
    
    cnts = [0] * (n + 1)
    cnts[n] = 1 # Make one final material
    while q:
        cur = q.popleft()

        for nxt, cnt in graph[cur]:
            # nxt can be made with cnt of cur
            cnts[nxt] += cnts[cur] * cnt

            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
            
    return cnts


if __name__ == '__main__':
    import sys; input = sys.stdin.readline
    
    n = int(input()) # number of materials n : [3, 100]
    m = int(input()) # number of relations m : [3, 100]

    graph = [[] for _ in range(n + 1)] # graph[x] = [(y, k), ...]
    indegree = [0] * (n + 1) # means that x can be made with k of y
    outdegree = [0] * (n + 1) # kinds of materials that can be made with i th material
    
    for _ in range(m): # assign relations
        x, y, k = map(int, input().split(' '))
        graph[x].append((y, k)) # x can be made with k of y
        outdegree[x] += 1 # -> check base materials
        indegree[y] += 1  # -> topology sort
    
    # cnts[i] : # number of i th material to make final material
    cnts = topological_sort(graph, indegree, n)
    for i in range(1, n):
        if outdegree[i] == 0 and cnts[i] > 0:
            print(i, cnts[i])