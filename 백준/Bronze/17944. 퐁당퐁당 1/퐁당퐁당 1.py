n, t = map(int, input().split())

targets = [i for i in range(1, 2 * n + 1)] + [i for i in range(2 * n -1, 1, -1)]
t = (t - 1) % (4 * n - 2)
print(targets[t])