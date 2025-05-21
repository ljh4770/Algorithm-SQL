def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    
    return int(num)

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    if n == 0:
        print(0)
        sys.exit(0)

    ranks = [int(input()) for _ in range(n)]
    ranks.sort()

    cut_off_num = my_round(15 / 100 * n)
    if cut_off_num > 0:
        ranks = ranks[cut_off_num:-cut_off_num]
        n -= 2 * cut_off_num
    
    avg = sum(ranks) / n
    print(my_round(avg))