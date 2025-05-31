def bellman_ford(edges, v, e, start):
    INF = float('inf')
    distance = [INF] * (v + 1) # Initialize distances to infinity
    distance[start] = 0 # Initialize the starting node's distance to 0
    
    # Iterate v times
    for i in range(v): # i == v - 1 for detecting negative cycles
        for j in range(e): # Relax all edges
            cur = edges[j][0]
            nxt = edges[j][1]
            w = edges[j][2]
            
            # If the current distance is not infinity and the next node's distance can be relaxed
            if distance[cur] != INF and distance[nxt] > distance[cur] + w:
                distance[nxt] = distance[cur] + w
                
                # Negative cycle detection
                if i == v - 1: # If it's the last iteration
                    return True, None

    return False, distance

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    # n: number of nodes, city
    # m: number of edges, bus
    n, m = map(int, input().split(' '))
    buses = [] # Directed edges with weights
    for _ in range(m):
        a, b, c = map(int, input().split(' '))
        buses.append((a, b, c))

    negative_cycle, distances = bellman_ford(buses, n, m, 1)
    
    if negative_cycle == True:
        print(-1)
    else:
        for i in range(2, n + 1):
            if distances[i] == float('inf'):
                print(-1)
            else:
                print(distances[i])