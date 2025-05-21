import sys

input = sys.stdin.readline

N = int(input().strip())
nums = [int(input().strip()) for _ in range(N)]

stack = []
res = []      # '+' 또는 '-' 기록
current = 1   # 다음 push에 사용할 값
valid = True  # 만들 수 있는지 여부

# nums 순서대로 처리
for num in nums:
    # 1) num에 도달할 때까지 push
    while current <= num:
        stack.append(current)
        res.append('+')
        current += 1
    
    # 2) 스택 최상단이 num과 동일한지 확인
    if stack and stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        valid = False
        break

# 결과 출력
if valid:
    print('\n'.join(res))
else:
    print("NO")
