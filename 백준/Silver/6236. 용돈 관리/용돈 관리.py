import sys
input = sys.stdin.readline

n, m = map(int, input().split())
spend = [int(input()) for _ in range(n)]

result = 0 # Answer: minimal number of withdrawals
start, end = min(spend), sum(spend)
while start <= end:
    # Temporary amount of money for a withdrawal
    mid = (start + end) // 2
    balance = mid # Init the balance
    cnt = 1 # Init withdrawal count

    for money in spend:
        if balance < money: # If the balance is LT the money to spend
            balance = mid # Withdraw money amount of mid
            cnt += 1 # Count the withdrawals
        # Spned the money for a day
        balance -= money

    # if withdrawals exceed m
    # or mid is less than the max spend
    if cnt > m or mid < max(spend):
        # Increase the mid value
        start = mid + 1
    else:
        result = mid # Update result
        # Decrease the mid value
        end = mid - 1

print(result)