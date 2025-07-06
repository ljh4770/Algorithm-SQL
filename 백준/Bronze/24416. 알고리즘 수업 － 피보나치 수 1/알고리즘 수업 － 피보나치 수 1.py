def fibo(n):
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    
    return b


if __name__ == "__main__":
    n = int(input())

    cnt = fibo(n)

    print(cnt, n - 2)