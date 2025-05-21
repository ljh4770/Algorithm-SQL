import sys
month, day = map(int, sys.stdin.readline().split(' '))

nums = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
week = ['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI']

res = (14 + day + nums[month - 1]) % 7
print(week[res])