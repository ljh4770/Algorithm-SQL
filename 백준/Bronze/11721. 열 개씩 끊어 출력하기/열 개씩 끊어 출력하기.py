import sys
input = sys.stdin.readline

string = input().rstrip()

for i in range(0, len(string), 10):
    print(string[i:i + 10])