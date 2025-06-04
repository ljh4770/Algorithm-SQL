def check_covered(posistions, height, n, m):
    # 1st light
    if height < posistions[0]:
        # If 1st light is not high enough to cover the start of the bridge
        return False
    # Intermediate lights
    for i in range(1, m):
        if posistions[i] - posistions[i - 1] > 2 * height:
            # If there are uncovered areas between neighbor lights
            return False
    # Last light
    if n - posistions[-1] > height:
        # If last light is not high enough to cover the end of the bridge
        return False
    
    return True

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input()) # Length of the bridge
    m = int(input()) # Number of the Lights
    pos = [*map(int, input().split())] # Ascending order

    result = 0 # Height of the lights
    start, end = 1, n
    while start <= end:
        # Temporary height
        mid = (start + end) // 2

        if check_covered(pos, mid, n, m) == True:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    print(result)