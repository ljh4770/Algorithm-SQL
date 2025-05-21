import sys
sys.setrecursionlimit(10**6)

def quadtree(n, vlist):
    s = 0
    for l in vlist:
        s += sum(l)
    
    if s == n**2:
        return '1'
    if s == 0:
        return '0'
    
    half = n//2
    temp = '('
    temp += quadtree(half,[l[:half] for l in vlist[:half]])
    temp += quadtree(half,[l[half:] for l in vlist[:half]])
    temp += quadtree(half,[l[:half] for l in vlist[half:]])
    temp += quadtree(half,[l[half:] for l in vlist[half:]])
    temp += ')'
    
    return temp

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    video = [[*map(int, input().rstrip())] for _ in range(n)]
    
    answer = quadtree(n, video)
    print(answer)