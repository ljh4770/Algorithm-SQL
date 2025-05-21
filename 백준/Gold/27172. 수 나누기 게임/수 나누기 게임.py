import sys
input = sys.stdin.readline

MAX = 10 ** 6 + 1

N = int(input())
num_list = list(map(int, input().split()))

nums = [-1] * MAX
for idx, num in enumerate(num_list):
    nums[num] = idx

score_list = [0] * N

for i in range(MAX) :
    if nums[i] > -1 :
        for j in range(i*2, MAX, i) :
            if nums[j] > -1 :
                score_list[nums[i]] += 1
                score_list[nums[j]] -= 1

print(*score_list)