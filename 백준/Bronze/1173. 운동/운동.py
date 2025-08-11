N, m, M, T, R = map(int, input().split())

if M - m < T:
    print(-1)
    exit()

cur_m = m
t_total = 0
t_exercise = 0
while t_exercise < N:
    t_total += 1
    if cur_m + T <= M: # do exercise
        cur_m += T
        t_exercise += 1
    else: # rest
        cur_m = max(m, cur_m - R)

print(t_total)