def count_ones(num):
    count = 0

    power = 0
    while 2**power <= num:
        p = 2**(power + 1)
        p_count = (num + 1) // p

        count += p_count * (p//2)

        left = (num + 1) % p
        count += max(0, left - p // 2)

        power += 1

    return count


if __name__ == '__main__':
    a, b = map(int, input().split(' '))

    print(count_ones(b) - count_ones(a - 1))