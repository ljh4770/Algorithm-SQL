import sys

def binary_search(A, q):
    l = 0
    h = len(A) - 1

    while l <= h:
        idx = (l + h) // 2
        if A[idx] == q:
            return True
        
        if A[idx] > q:
            h = idx - 1
        else:
            l = idx + 1

    return False
        

N  = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
M  = int(sys.stdin.readline().strip())
Q = list(map(int, sys.stdin.readline().strip().split()))

A.sort()
for q in Q:
    if binary_search(A, q) == True:
         print(1)
    else:
         print(0)