from collections import deque

def josephus_deque(N, K):
    dq = deque(range(1, N+1))  # [1, 2, 3, ..., N]
    result = []

    while dq:
        # (K-1)번 앞 사람을 빼서 뒤에 붙인다.
        for _ in range(K-1):
            front = dq.popleft()
            dq.append(front)
        # 이제 맨 앞 사람이 '제거될 사람'이므로 pop
        result.append(dq.popleft())

    return result

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.readline().strip()
    N, K = map(int, input_data.split())

    res = josephus_deque(N, K)
    # 출력 형식: <3, 6, 2, 7, 5, 1, 4> 와 같은 형태
    print("<" + ", ".join(map(str, res)) + ">")
