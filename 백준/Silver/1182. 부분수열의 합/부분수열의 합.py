def tracking(cur, sum_):
    global n, s, nums, cnt
    if cur >= n: # End condition
        return

    sum_ += nums[cur]

    if sum_ == s:
        cnt += 1
    
    tracking(cur + 1, sum_)
    tracking(cur + 1, sum_ - nums[cur])

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, s = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    cnt = 0

    tracking(0, 0)
    print(cnt)