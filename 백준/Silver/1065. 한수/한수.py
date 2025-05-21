def get_digits(num):
    return list(map(int, str(num)))

def get_diff(digits):
    res = []

    for i in range(len(digits) - 1):
        diff = digits[i] - digits[i + 1]
        res.append(diff)

    return res

if __name__ == '__main__':
    import sys

    N = int(sys.stdin.readline())

    cnt = 0
    for num in range(1, N + 1, 1):
        digits = get_digits(num)
        diffs = get_diff(digits)

        if len(diffs) <= 1 or len(set(diffs)) == 1:
            cnt += 1
    print(cnt)