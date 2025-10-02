if __name__ == "__main__":
    m, n = map(int, input().split())
    if m > n: #세로가 길때
        print(n*2-1)
    else: #가로가 길때
        print(m*2-2)

    if m==n:
        if m % 2==1: #홀수
            print(m//2+1, m//2+1)
        else:
            print(m//2+1, m//2)
    else:
        if m > n:
            if n % 2==1: #홀수
                print(n//2+1+(m-n), n//2+1)
            else:
                print(n//2+1, n//2)
        else:
            if m % 2==1:
                print(m//2+1, m//2+1+(n-m))
            else:
                print(m//2+1, m//2)