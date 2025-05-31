import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

arr_sum = set()
for x in arr:
    for y in arr:
        arr_sum.add(x+y)

answer = 0
flag = False
for i in range(n-1, -1, -1):
    for j in range(i+1):
        if arr[i]-arr[j] in arr_sum:
            answer = arr[i]
            flag = True
            break
    if flag == True:
        break

print(answer)