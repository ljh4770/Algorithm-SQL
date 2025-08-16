import sys; input = sys.stdin.readline

n = int(input()) # n : [1, 10]
# price for each number
prices = [*map(int, input().split())] # p : [1, 50]
m = int(input()) # m : [1, 50] - budget

dp = [''] * (m + 1) # Room number that afford with i money

for i in range(1, m + 1, 1):
    candidates = [] # Candidate room numbers for cuurent budget
    for num, p in enumerate(prices): # append 'num' if possible
        if i - p < 0: # Cannot buy the number
            continue
        room_number = dp[i - p] + str(num)
        if room_number:
            candidate = int(room_number)
            candidates.append(candidate)
    if candidates:
        dp[i] = str(max(candidates))

print(dp[m])