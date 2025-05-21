import sys

input = sys.stdin.readline

N, M = map(int, input().split())
name_to_num = dict()
num_to_name = list()


for i in range(N):
    name = input().strip()
    name_to_num[name] = i + 1
    num_to_name.append(name)

for _ in range(M):
    query = input().strip()
    if query.isdigit() == True:
        num = int(query)
        print(num_to_name[num - 1])
    else:
        print(name_to_num[query])