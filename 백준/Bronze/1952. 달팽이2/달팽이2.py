if __name__ == "__main__":
    m, n = map(int, input().split())
    
    base = 2 * (max(m, n) - 1)
    if m > n:
        base -= 2 * (m - n)
        base += 1
    elif m < n:
        base -= 2 * (n - m)

    print(base)