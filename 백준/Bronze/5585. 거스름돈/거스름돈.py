import sys
value = int(sys.stdin.readline())
coins = [500, 100, 50, 10, 5, 1]

change = 1000 - value
cnt = 0

for coin in coins:
    if change // coin > 0:
        cnt += change // coin
        change %= coin
    if change == 0:
        break
print(cnt)