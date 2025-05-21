def sol(arr1, arr2, res = []):
    if (not arr1) or (not arr2):
        return res
    
    tmp1, tmp2 = max(arr1), max(arr2)
    idx1, idx2 = arr1.index(tmp1), arr2.index(tmp2)

    if tmp1 == tmp2:
        res.append(tmp1)
        return sol(arr1[idx1 + 1:], arr2[idx2 + 1:], res)
    elif tmp1 > tmp2:
        arr1.pop(idx1)
        return sol(arr1, arr2, res)
    else:
        arr2.pop(idx2)
        return sol(arr1, arr2, res)

import sys
input = sys.stdin.readline

n = int(input())
arr1 = [*map(int, input().split(' '))]
m = int(input())
arr2 = [*map(int, input().split(' '))]

sub = sol(arr1, arr2)

k = len(sub)
print(k)
if k == 0:
    sys.exit(0)
else:
    print(*sub)