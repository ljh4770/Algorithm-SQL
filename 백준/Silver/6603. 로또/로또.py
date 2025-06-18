import sys
sys.setrecursionlimit(10 ** 9 + 1)

def lotto(k, depth, start):
    if depth == 6:
        answer = [s[i] for i in range(k) if visited[i]]
        print(*answer)
        return
    
    for i in range(start, k, 1):
        if visited[i] == False:
            visited[i] = True
            lotto(k, depth + 1, i + 1)
            visited[i] = False
    

if __name__ == "__main__":
    input = sys.stdin.readline

    while True:
        input_arr = [*map(int, input().split(' '))]
        k, s = input_arr[0], input_arr[1:]
        if k == 0:
            break
        
        visited = [False] * k
        lotto(k, 0, 0)
        print()