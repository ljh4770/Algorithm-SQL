def solve():
    n, m = map(int, input().split(' '))
    arr_a = [*map(int, input().split(' '))]
    arr_b = [*map(int, input().split(' '))]
    
    arr_a.sort()
    arr_b.sort()

    start = 0 # Iterate to arr_b
    count = 0 # Answer: Number of pairs (a, b) s.t. a > b
    for i in range(n): # Iterate to arr_a
        while True:
            if start == m or arr_a[i] <= arr_b[start]:
                count += start
                break
            else:
                start += 1
                
    print(count)


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        solve()