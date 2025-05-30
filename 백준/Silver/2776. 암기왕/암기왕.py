import sys

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0


def solve():
    n = int(input())
    note1 = [*map(int, input().split(' '))]
    m = int(input())
    note2 = [*map(int, input().split(' '))]

    note1.sort()
    for target in note2:
        print(binary_search(note1, target))


if __name__ == "__main__":
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        solve()