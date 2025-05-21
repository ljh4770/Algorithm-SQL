if __name__ == "__main__":
    import sys
    import math

    N, M = map(int, sys.stdin.readline().split())

    is_prime = [True] * (M + 1)
    is_prime[0] = False
    is_prime[1] = False

    for num in range(2, int(math.sqrt(M)) + 1, 1):
        if is_prime[num] == True:
            for mult in range(num * num, M + 1, num):
                is_prime[mult] = False

    for num in range(N, M + 1, 1):
        if is_prime[num] == True:
            print(num)