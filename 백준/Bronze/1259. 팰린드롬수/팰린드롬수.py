def is_palindrome(num):
    return num == num[::-1]

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    while True:
        n = input().rstrip()
        if n == '0':
            break
        
        if is_palindrome(n) == True:
            print('yes')
        else:
            print('no')