import sys
input = sys.stdin.readline

s = input().rstrip()

counts = [0] * 26

for c in s:
    counts[ord(c) - ord('a')] += 1

for c in counts:
    print(c, end=' ')
print()