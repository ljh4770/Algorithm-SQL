def solution(info, n, m):
    INF = float('inf')
    N = len(info)
    
    dp = [[INF] * n for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(N):
        a_i, b_i = info[i]
        for a in range(n):
            if dp[i][a] == INF:
                continue  # 도달할 수 없는 상태는 건너뛰기

            # 1. A 도둑이 아이템 i를 훔치는 경우
            new_a = a + a_i
            if new_a < n:  # A의 누적 흔적이 n 미만이어야 함
                dp[i + 1][new_a] = min(dp[i + 1][new_a], dp[i][a])
            
            # 2. B 도둑이 아이템 i를 훔치는 경우
            new_b = dp[i][a] + b_i
            if new_b < m:  # B의 누적 흔적이 m 미만이어야 함
                dp[i + 1][a] = min(dp[i + 1][a], new_b)
    
    # 모든 아이템을 고려한 후, 유효한 상태(두 도둑 모두 안전)에서 A의 흔적의 최솟값을 찾음
    answer = INF
    for a in range(n):
        if dp[N][a] < m:
            answer = min(answer, a)
    
    return answer if answer != INF else -1