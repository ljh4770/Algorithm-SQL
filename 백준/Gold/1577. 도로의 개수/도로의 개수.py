def road_to_base(a, b, c, d, base):
    return a + b * base + c * base ** 2 + d * base ** 3

if __name__ == "__main__":
    import sys; sys.stdin.readline

    # n, m : [1, 100]
    # n - Horizontal Length / m - Vertical Length
    n, m = map(int, input().split())
    k = int(input()) # k : [1, 50] - number of roads on construction
    # (a, b, c, d) - road from (a, b) to (c, d) , cf) (n, m)
    const_info = set()
    BASE = 100
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        # guarantee for (a, b) < (c, d)
        if a > c:
            a, c = c, a 
        elif b > d:
            b, d = d, b
        
        # make 100-base number (a + b * 100 + c * 100 ** 2 + d * 100 ** 3)
        road_num = road_to_base(a, b, c, d, BASE)
        const_info.add(road_num)

    # number of cases to reach the road(=the element of the matrix)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1 # Base case

    # Fill in the horizontal elements with a row at index 0
    for c in range(1, n + 1, 1):
        road_num = road_to_base(c - 1, 0, c, 0, BASE)
        if road_num in const_info: # road on construction
            break
        dp[0][c] += dp[0][c - 1]

    # Fill in the vertical elements with a column at index 0
    for r in range(1, m + 1, 1):
        road_num = road_to_base(0, r - 1, 0, r, BASE)
        if road_num in const_info: # road on construction
            break
        dp[r][0] += dp[r - 1][0]
        
    for c in range(1, n + 1, 1):
        for r in range(1, m + 1, 1):
            # check below road & left road
            # -> upper & left element in the matrix

            # Upper
            road_num = road_to_base(c, r - 1, c, r, BASE)
            if road_num not in const_info: # road is passable
                dp[r][c] += dp[r - 1][c]
            # left
            road_num = road_to_base(c - 1, r, c, r, BASE)
            if road_num not in const_info: # road is passable
                dp[r][c] += dp[r][c - 1]
    print(dp[m][n])        