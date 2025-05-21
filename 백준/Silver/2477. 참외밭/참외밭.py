import sys

input = sys.stdin.readline

k = int(input())
vectors = [tuple(map(int, input().split(' '))) for _ in range(6)]
horizon = []
vertical = []
total = []

for d, length in vectors:
    total.append(length)
    if d in [1, 2]:
        horizon.append(length)
    elif d in [3, 4]:
        vertical.append(length)

outer = max(horizon) * max(vertical)
max_h_idx = total.index(max(horizon))
max_v_idx = total.index(max(vertical))

inner1 = abs(total[max_h_idx - 1] - total[(max_h_idx - 5 if max_h_idx == 5 else max_h_idx + 1)])
inner2 = abs(total[max_v_idx - 1] - total[(max_v_idx - 5 if max_v_idx == 5 else max_v_idx + 1)])
area = outer - (inner1 * inner2)
print(area * k)