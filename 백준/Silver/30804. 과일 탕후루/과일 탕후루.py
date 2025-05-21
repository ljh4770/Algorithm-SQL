import sys
input = sys.stdin.readline

N = int(input())
candy = list(map(int, input().split(' ')))

answer = 0
a = 0
cnt = dict()
distinct_cnt = 0

for b in range(0, N, 1):
    if candy[b] in cnt.keys():
        cnt[candy[b]] += 1
    else:
        cnt[candy[b]] = 1
        distinct_cnt += 1
    
    while distinct_cnt > 2:
        cnt[candy[a]] -= 1
        if cnt[candy[a]] == 0:
            del cnt[candy[a]]
            distinct_cnt -= 1
        a += 1
    answer = max(answer, b - a + 1)

print(answer)