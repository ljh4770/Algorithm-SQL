import sys; input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]
arr.sort()

result = (0, 0) # value pair s.t. sum is closest to pivot(0)
best_value = float('inf') # absolute sum
l, r = 0, n - 1 # two pointer for the arr
while l < r:
    left_value, right_value = arr[l], arr[r]
    sum_ = left_value + right_value
    cur_value = abs(sum_)

    # Update the absolute sum if improved
    if cur_value <= best_value:
        best_value = cur_value
        result = (left_value, right_value)
    
    # move pointer toward zero
    if sum_ <= 0:
        l += 1
    else:
        r -= 1
    
print(*result)