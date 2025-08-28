def solve(sub_str, main_str):
    i, j = 0, 0

    while i < len(sub_str) and j < len(main_str):
        if sub_str[i] == main_str[j]:
            i += 1
        j += 1
    
    if i == len(sub_str):
        print("Yes")
    else:
        print('No')

if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        s, t = line.strip().split()
        
        solve(s, t)