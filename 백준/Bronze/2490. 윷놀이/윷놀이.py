inputs = [map(int, input().split()) for _ in range(3)]

results = []

for abc in inputs:
    res = sum(abc)

    if res == 0:
        results.append("D")
    elif res == 1:
        results.append("C")
    elif res == 2:
        results.append("B")
    elif res == 3:
        results.append("A")
    elif res == 4:
        results.append("E")

for i in range(3):
    print(results[i])