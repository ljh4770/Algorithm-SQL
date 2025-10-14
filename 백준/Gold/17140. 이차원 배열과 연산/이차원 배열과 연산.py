from collections import Counter

def count_sort(arr):
    num_cnt = Counter(arr)
    num_cnt = sorted(num_cnt.items(), key=lambda x: (x[1], x[0]))

    res = []
    for num, cnt in num_cnt:
        if num == 0:
            continue
        res += [num, cnt]

    return res

def r_sort(arr):
    max_len = 0
    res_arr = []

    for row in arr:
        row = count_sort(row)
        max_len = max(max_len, len(row))
        res_arr.append(row)

    for i in range(len(arr)):
        if len(res_arr[i]) <= 100:
            cur_len = len(res_arr[i])
            res_arr[i] += [0] * (max_len - cur_len)
        else:
            res_arr[i] = res_arr[i][:100]

    return res_arr

def c_sort(arr):
    c = len(arr[0])
    max_len = 0
    row_arr = []

    for ci in range(c):
        col = [row[ci] for row in arr]
        col = count_sort(col)
        max_len = max(max_len, len(col))
        row_arr.append(col)
    
    max_len = min(100, max_len)
    res_arr = [[0] * c for _ in range(max_len)]
    for ci, col in enumerate(row_arr):
        for ri, num in enumerate(col):
            if ri >= 100:
                break
            res_arr[ri][ci] = num

    return res_arr


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    r, c, k = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(3)]

    time = 0
    r, c = r - 1, c - 1
    while time <= 100:
        if 0 <= r < len(arr) and 0 <= c < len(arr[0]):
            if arr[r][c] == k:
                print(time)
                break
        
        if len(arr) >= len(arr[0]):
            arr = r_sort(arr)
        else:
            arr = c_sort(arr)
        
        time += 1
    else:
        print(-1)