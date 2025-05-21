def bellman_ford():
    global distance, edges, n

    for i in range(n):
        for cur, next, cost in edges:
            if distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == n - 1:
                    return True
    return False

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    tc = int(input())

    for _ in range(tc):
        n, m, w = map(int, input().split(' '))
        edges = []

        for _ in range(m):
            s, e, t = map(int, input().split(' '))
            edges.append((s, e, t))
            edges.append((e, s, t))
        for _ in range(w):
            s, e, t = map(int, input().split(' '))
            edges.append((s, e, -t))
            
        distance = [0] * (n + 1)
        if bellman_ford() == True:
            print("YES")
        else:
            print("NO")