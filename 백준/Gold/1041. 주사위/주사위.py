n = int(input()) # N : [1, 10 ** 6]
# number of faces
numbers = [*map(int, input().split())] # [A, B, C, D, E, F] : [1, 50]

if n == 1:
    answer = sum(numbers) - max(numbers)
else:
    # (A, F), (B, E), (C, D) : opposite faces
    # > (0, 5), (1, 4), (2, 3) index
    opposite_faces = [(0, 5), (1, 4), (2, 3)]

    # n ** 2 numbers for each face
    # total 5 faces
    # minimize the sum of faces

    smaller_num = [] # append smaller numbers from opposite faces
    for idx_pair in opposite_faces:
        smaller = min(numbers[idx] for idx in idx_pair)
        smaller_num.append(smaller)
    a, b, c = sorted(smaller_num) # a <= b <= c


    answer = 0
    # two sides
    answer += 2 * a * (n ** 2)

    # the other two sides
    answer += 2 * (
        a * n * (n - 2)
        + 2 * b * n
    )

    # top face
    answer += (
        a * (n - 2) * (n - 2)
        + 4 * b * (n - 2)
        + 4 * c
    )

print(answer)