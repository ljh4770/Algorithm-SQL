def merge_sort(arr):
    if len(arr) < 2:
        return arr, 0

    cnt = 0
    mid = len(arr) // 2
    low_arr, tmp = merge_sort(arr[:mid])
    cnt += tmp
    high_arr, tmp = merge_sort(arr[mid:])
    cnt += tmp

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] <= high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            cnt +=  (len(low_arr) - l)
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    
    return merged_arr, cnt


import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split(' ')))
arr_sorted, cnt = merge_sort(arr)
# print(arr_sorted)
print(cnt)