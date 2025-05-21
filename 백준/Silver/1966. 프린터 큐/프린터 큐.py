from queue import Queue

def priority_printer(N, M, priority):
    q = Queue()
    max_p = max(priority)

    cnt = 0

    for i, p in enumerate(priority):
        q.put((i, p))
    
    while not q.empty():
        crt_list = list(q.queue)
        max_p = max(crt_list, key=lambda x: x[1])[1]

        idx, front_p = q.get()

        if front_p < max_p:
            q.put((idx, front_p))
        else:
            cnt += 1
            if idx == M:
                print(cnt)
                return None

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        priority = list(map(int, input().split()))
        priority_printer(N, M, priority)
