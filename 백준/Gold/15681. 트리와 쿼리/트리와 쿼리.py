import sys
sys.setrecursionlimit(10**6)

def makeTree(currentNode, parent) :
    global connect, child

    for node in connect[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            makeTree(node, currentNode)

def countSubtreeNodes(currentNode) :
    global size
    size[currentNode] = 1
    for node in child[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]

if __name__ == "__main__":
    input = sys.stdin.readline

    n, r, q = map(int, input().split(' '))

    edges = [tuple(map(int, input().split(' '))) for _ in range(n - 1)]
    queries = [int(input()) for _ in range(q)]

    connect = [[] for _ in range(n + 1)]
    for u, v in edges :
        connect[u].append(v)
        connect[v].append(u)
    
    child = [[] for _ in range(n + 1)]
    makeTree(r, 0)
    size = [0] * (n + 1)
    countSubtreeNodes(r)
    for u in queries:
        print(size[u])