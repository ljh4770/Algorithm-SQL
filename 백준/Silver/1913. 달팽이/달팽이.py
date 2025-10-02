if __name__ == '__main__':
    n = int(input()) # n : [3, 999]
    k = int(input()) # k : [1, n ** 2]

    snail = [[0] * n for _ in range(n)]
    even = [(0, 1), (1, 0)]
    odd = [(0, -1), (-1, 0)]

    q, r = divmod(n, 2)
    x, y = q, q + r - 1

    snail[x][y] = 1
    coord = (x, y)
    for i in range(2, n + 1, 1):
        num = (i - 1) ** 2 + 1
        r = num % 2
        x = x - 1 if r == 0 else x + 1
        directions = even if r == 0 else odd
        
        snail[x][y] = num
        if num == k:
                coord = (x, y)

        dx, dy = directions[0]
        for _ in range(i - 1):
            x, y = x + dx, y + dy
            num += 1
            
            snail[x][y] = num
            if num == k:
                coord = (x, y)
        
        dx, dy = directions[1]
        for _ in range(i - 1):
            x, y = x + dx, y + dy
            num += 1
            
            snail[x][y] = num
            if num == k:
                coord = (x, y)

    for row in snail:
        print(*row)
    
    print(*map(lambda x: x + 1, coord))