from typing import List

def check_digit(target: str) -> List[int]:
    # compare digit and the board to decide possibility

    # string form of each digit
    string_digits =[
        "####.##.##.####", # 0
        "..#..#..#..#..#", # 1
        "###..#####..###", # 2
        "###..####..####", # 3
        "#.##.####..#..#", # 4
        "####..###..####", # 5
        "####..####.####", # 6
        "###..#..#..#..#", # 7
        "####.#####.####", # 8
        "####.####..####"  # 9
    ]
    result = []

    for d, digit in enumerate(string_digits):
        for i in range(3 * 5):
            # board is on and digit is off -> impossible digit
            if target[i] == '#' and digit[i] == '.':
                break
        else:
            # append possible digit
            result.append(d)
    
    return result


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n = int(input()) # n : [1, 9]

    # number board
    # 5 x 3 for each digit
    # length for each line is 4n - 1 -> 3n + (n - 1)
    board = [input().rstrip() for _ in range(5)]

    # possible number for each digit
    possible_digits = [[] for _ in range(n)]
    for i in range(n): # for each digit
        c = 4 * i # start index of the column
        target = ''
        for j in range(5): # for each line of a digit
            # make each digit as a string
            target += board[j][c:c + 3]
        
        possible_digits[i] = check_digit(target)

    for i in range(n):
        # there is no possible number
        if len(possible_digits[i]) == 0:
            print(-1)
            break
    else:
        # calcualte the mean
        answer = 0 # the mean
        for i in range(n): # for each digit
            pass
            p = len(possible_digits[i]) ** -1
            mu = sum(possible_digits[i]) * p
            scale = 10 ** (n - i - 1) # scale for each digit
            answer += mu * scale
        print(answer)