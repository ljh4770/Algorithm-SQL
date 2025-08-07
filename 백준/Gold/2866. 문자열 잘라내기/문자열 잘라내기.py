import sys; input = sys.stdin.readline

r, c = map(int, input().split())
table = [list(input().rstrip()) for _ in range(r)]

result = 0 # row index that makes repeated column string on table
start, end = 0, r - 1 # index range for row
while start <= end:
    mid = (start + end) // 2

    
    flag = False # True if there exist repeated column string
    check = set() # set to store unique column strings
    for j in range(c):
        substr = ''
        for i in range(mid, r):
            substr += table[i][j]
        if substr in check:
            flag = True
            break
        check.add(substr)
        
    if flag:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)