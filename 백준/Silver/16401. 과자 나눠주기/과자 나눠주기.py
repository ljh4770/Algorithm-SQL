import sys
input = sys.stdin.readline

# m: number of children
# n: number of cookies
m, n = map(int, input().split(' '))
cookies = [*map(int, input().split(' '))] # Length of cookies

max_length = 0 # 0 denote distributing is impossible
start, end = 1, max(cookies)
while start <= end:
    # Temporary length of cookie
    mid = (start + end) // 2
    cnt = 0 # Number of cookies with same length, mid

    # Iterate thorough cookies
    for length in cookies:
        if length >= mid: # Cookie can be sliced
            cnt += length // mid
    
    if cnt >= m:  # If the number of cookies is enough
        max_length = mid
        start = mid + 1
    else:  # If the number of cookies is not enough
        end = mid - 1
        
print(max_length)