def merge_sort(arr, items):
    if len(arr) < 2:
        return arr, items

    mid = len(arr) // 2
    low_arr, low_item = merge_sort(arr[:mid], items[:mid])
    high_arr, high_item = merge_sort(arr[mid:], items[mid:])

    merged_arr = []
    merged_item = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] <= high_arr[h]:
            merged_arr.append(low_arr[l])
            merged_item.append(low_item[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            merged_item.append(high_item[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    merged_item += low_item[l:]
    merged_item += high_item[h:]
    return merged_arr, merged_item

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    ages = []
    names = []
    for _ in range(n):
        age, name = input().rstrip().split(' ')
        ages.append(int(age))
        names.append(name)

    ages, names = merge_sort(ages, names)
    for age, name in zip(ages, names):
        print(age, name)