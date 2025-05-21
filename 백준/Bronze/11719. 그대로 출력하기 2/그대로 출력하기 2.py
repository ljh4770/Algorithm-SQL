import sys

strings = []
for line in sys.stdin:  # EOF까지 읽는다
    line = line[:-1]
    print(line)