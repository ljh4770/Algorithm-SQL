a, b = map(int, input().split())

while (a, b) != (0, 0):
    print("Yes" if a > b else "No")
    a, b = map(int, input().split())