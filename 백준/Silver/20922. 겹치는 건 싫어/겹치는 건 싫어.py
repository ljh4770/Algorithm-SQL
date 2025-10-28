n, k = map(int, input().split())
arr = [*map(int, input().split())]

MAX_LEN = 100_000
num_cnt = [0] * (MAX_LEN + 1)

answer = 0
start, end = 0, 0
while end < n:
    if num_cnt[arr[end]] >= k:
        num_cnt[arr[start]] -= 1
        start += 1
    else:
        num_cnt[arr[end]] += 1
        end += 1
        answer = max(answer, end - start)

print(answer)