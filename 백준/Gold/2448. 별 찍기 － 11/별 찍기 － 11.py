def fractal(i, j, size):
    global triangle
    
    if size == 3:# mark start for the base case
        triangle[i][j] = '*'
        triangle[i + 1][j - 1] = "*"
        triangle[i + 1][j + 1] = "*"
        for k in range(-2, 3, 1):
            triangle[i + 2][j - k] = "*"
    else: # divide case with reducing size
            new_size = size//2
            fractal(i, j, new_size)
            fractal(i + new_size, j - new_size, new_size)
            fractal(i + new_size, j + new_size, new_size)

import sys
# n is guaranteed to be 3 * 2 ^ k
# k is an integer ranging from 0 to 10, inclusive
n = int(sys.stdin.readline())
triangle = [[' '] * 2 * n for _ in range(n)]
fractal(0, n - 1, n)

for star in triangle:
    print("".join(star))