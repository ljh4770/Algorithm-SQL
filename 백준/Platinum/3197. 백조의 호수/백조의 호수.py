from collections import deque

DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

def solve():
    import sys
    input = sys.stdin.readline
    r, c = map(int, input().split())
    lake = [list(input().rstrip()) for _ in range(r)]
    swans = []
    water_q = deque()
    
    # 초기화: 백조 위치, 물 큐
    for i in range(r):
        for j in range(c):
            if lake[i][j] == 'L':
                swans.append((i,j))
                lake[i][j] = '.'
            if lake[i][j] == '.':
                water_q.append((i,j))
    
    # 큐와 방문 배열 준비
    visited_water = [[False]*c for _ in range(r)]
    visited_swan  = [[False]*c for _ in range(r)]
    swan_q        = deque([swans[0]])
    swan_next_q   = deque()
    water_next_q  = deque()
    visited_swan[swans[0][0]][swans[0][1]] = True
    
    day = 0
    # 두 번째 백조 좌표
    target = swans[1]
    
    # 메인 루프
    while True:
        # 1) 백조 확장
        while swan_q:
            x,y = swan_q.popleft()
            if (x,y) == target:
                print(day)
                return
            for dx,dy in DIRECTIONS:
                nx, ny = x+dx, y+dy
                if not (0<=nx<r and 0<=ny<c): continue
                if visited_swan[nx][ny]: continue
                visited_swan[nx][ny] = True
                if lake[nx][ny] == 'X':
                    swan_next_q.append((nx,ny))
                else:
                    swan_q.append((nx,ny))
        
        # 2) 물로 얼음 녹이기
        while water_q:
            x,y = water_q.popleft()
            for dx,dy in DIRECTIONS:
                nx, ny = x+dx, y+dy
                if not (0<=nx<r and 0<=ny<c): continue
                if visited_water[nx][ny]: continue
                visited_water[nx][ny] = True
                if lake[nx][ny] == 'X':
                    lake[nx][ny] = '.'
                    water_next_q.append((nx,ny))
                else:
                    water_q.append((nx,ny))
        
        # 3) 큐 교체 및 일수 증가
        swan_q, swan_next_q = swan_next_q, deque()
        water_q, water_next_q = water_next_q, deque()
        day += 1

if __name__ == "__main__":
    solve()
