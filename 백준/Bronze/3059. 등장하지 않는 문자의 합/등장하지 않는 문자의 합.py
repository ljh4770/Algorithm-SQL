import sys; input = sys.stdin.readline

ALPHABET = {chr(i) for i in range(65, 91, 1)}

def solve(s):
    remainder = ALPHABET.difference(set(s))
    answer = 0
    for c in remainder:
        answer += ord(c)
    
    print(answer)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().rstrip()
        solve(s)