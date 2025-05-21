x, y, w, h = map(int, (input().split(' ')))
vertical_min = min(abs(x - 0), abs(x - w))
horizontal_min = min(abs(y - 0), abs(y - h))
print(min(vertical_min, horizontal_min))