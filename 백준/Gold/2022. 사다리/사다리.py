# x, y, c : (0, 3 * 10 ** 9]
x, y, c = map(float, input().split())
# Prepare for square operation
x_sq = x ** 2
y_sq = y ** 2

# Binary Search for interval distance of two buildings
width = 0
start, end = 0.000001, max(x, y)
for scale in range(4, 6 + 1):
    s = 0.1 ** scale
    while end - start >= s:
        mid = (start + end) / 2
        # print(f"{s:.6f} --- {start:.6f} {mid:.6f} {end:.6f}, {width:.6f}")

        # Too long(longer than hypotenuse)
        if x < mid or y < mid:
            end = mid - s
            continue

        # Heights of each triangle
        h_x = (x_sq - mid ** 2) ** 0.5
        h_y = (y_sq - mid ** 2) ** 0.5

        # derived by area ratio
        calc = c * (1 / h_x + 1 / h_y)
        if calc == 1: # Just Right
            width = mid
        elif calc <= 1: # Too Long
            width = mid
            start = mid + s
        else: # Too Short
            end = mid - s
print(f"{width:.3f}")