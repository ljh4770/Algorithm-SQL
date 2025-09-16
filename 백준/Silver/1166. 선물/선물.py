n, l, w, h = map(int, input().split())

left, right = 0, min(l, w, h)
a = right
for _ in range(100):
    mid = (left + right) / 2

    l_cnt = l // mid
    w_cnt = w // mid
    h_cnt = h // mid
    cnt = l_cnt * w_cnt * h_cnt
    if cnt >= n:
        left = mid
        a = mid
    else:
        right = mid

print(float(a))