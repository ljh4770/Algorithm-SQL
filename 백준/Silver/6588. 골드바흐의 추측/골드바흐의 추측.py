import sys; input = sys.stdin.readline

MAX_LEN = 1000001
numbers = [True] * MAX_LEN
numbers[0] = numbers[1] = False

m = int(MAX_LEN ** 0.5)
for i in range(2, m + 1):
    if numbers[i]:
        for k in range(2 * i, MAX_LEN, i):
            numbers[k] = False

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(n - 3, 2, -2):
        if (numbers[i] == True) and (numbers[n - i] == True):
            print(f"{n} = {n-i} + {i}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')