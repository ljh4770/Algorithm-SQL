def tracking(k, idx):
    global n, m, nums

    if k == m:
        for i in range(m):
            print(answer[i], end=' ')
        print()
        return

    temp = 0
    for i in range(idx, n):
        if temp != nums[i]:
            answer[k] = nums[i]
            temp = nums[i]
            tracking(k + 1, i)

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))
    nums.sort()

    answer = [-1] * m

    tracking(0, 0)