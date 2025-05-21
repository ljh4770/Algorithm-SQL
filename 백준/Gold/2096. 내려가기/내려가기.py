import sys
input = sys.stdin.readline

n = int(input())

# Each index assume that number is selected for the step
case_min = [[0, 0, 0] for _ in range(2)]
case_max = [[0, 0, 0] for _ in range(2)]

for i in range(1, n + 1, 1):
    nums = list(map(int, input().split(' ')))
    # -----Consider Minimum Case-----
    # Selecting first number
    case_min[1][0] = nums[0]
    case_min[1][0] += min(case_min[0][0], case_min[0][1])
    # Selecting second number
    case_min[1][1] = nums[1]
    case_min[1][1] += min(case_min[0][0], case_min[0][1], case_min[0][2])
    # Selecting third number
    case_min[1][2] = nums[2]
    case_min[1][2] += min(case_min[0][1], case_min[0][2])
    
    # -----Consider Maximum Case-----
    # Selecting first number
    case_max[1][0] = nums[0]
    case_max[1][0] += max(case_max[0][0], case_max[0][1])
    # Selecting second number
    case_max[1][1] = nums[1]
    case_max[1][1] += max(case_max[0][0], case_max[0][1], case_max[0][2])
    # Selecting third number
    case_max[1][2] = nums[2]
    case_max[1][2] += max(case_max[0][1], case_max[0][2])

    for j in range(0, 3, 1): # Overwrite
        case_min[0][j] = case_min[1][j]
        case_max[0][j] = case_max[1][j]

print(max(case_max[1]), min(case_min[1]))