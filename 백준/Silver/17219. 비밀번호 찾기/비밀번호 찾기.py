import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
data = [tuple(input().strip().split(' ')) for _ in range(N)]
adds = [input().strip() for _ in range(M)]
mapping = dict()

for add, site in data:
    mapping[add] = site

for add in adds:
    print(mapping[add])