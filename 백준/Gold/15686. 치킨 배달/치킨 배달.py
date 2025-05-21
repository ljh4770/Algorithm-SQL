import sys
sys.setrecursionlimit(10**8)

N,M = map(int,input().split()) # N은 격자 사이즈, M은 치킨집 개수
graph = []
house = []
chicken = []


for col in range(N):
    graph.append(list(map(int,input().split())))
    for row in range(N):
        if graph[col][row] == 1:
            house.append((col,row))
            
        elif graph[col][row] == 2:
            chicken.append((col,row))


arr = []
real_check = int(1e9)
def back(num,cnt):
    global real_check
    if num>len(chicken):
        return
    
    if cnt==M:
        result_tot = 0
        for hx,hy in house:
            min_check = int(1e9)
            for idx in arr:
                cx,cy = chicken[idx]
                min_check = min(min_check,abs(hx-cx)+abs(hy-cy))
                
            result_tot+=min_check
            
        real_check = min(result_tot,real_check)
        return

    arr.append(num)
    back(num+1,cnt+1)
    arr.pop()
    back(num+1,cnt)
    return real_check

print(back(0,0))