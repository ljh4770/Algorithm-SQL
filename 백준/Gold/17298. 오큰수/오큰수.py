import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = [-1] * N  # 결과 배열을 -1로 초기화
stack = []  # 인덱스를 저장할 스택

for i in range(N):
    # 스택이 비어있지 않고, 현재 원소가 스택 top의 원소보다 큰 경우
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(" ".join(map(str, result)))
