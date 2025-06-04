# bisect_left
def binarySearch(arr, x):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = [*map(int,input().split())]
    
    LIS = [arr[0]]
    for num in arr:
        if num > LIS[-1]: # Increasing order
            LIS.append(num)
        else: # Equal or smaller
            idx = binarySearch(LIS, num)
            LIS[idx] = num
    
    print(len(LIS))
    # Result arr may noy be the True LIS, but its length is the same as the True LIS
    # ex) arr = [10, 20, 30, 15, 50]
    # -> result: [10, 15, 30, 50]
    # -> True LIS: [10, 20, 30, 50]