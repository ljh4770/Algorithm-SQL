def d(n):
    return n + sum(map(int, str(n)))

self_num = set(range(1, 10000 + 1))
generated_num = set()

for num in self_num:
    generated_num.add(d(num))

self_num -= generated_num

for num in sorted(self_num):
    print(num)