# 다각형의 면적
n = int(input())
figure = []

for _ in range(n):
    figure.append(list(map(int,input().split(' '))))
figure.append(figure[0])

answer = 0
for i in range(n):
    answer += figure[i][0]*figure[i+1][1] - figure[i+1][0]*figure[i][1]

print(abs(answer)/2)