from collections import Counter

room_no = input()

num_cnt = Counter(room_no)
numbers = [str(i) for i in range(10)]

num_cnt['6'] = (num_cnt['6'] + num_cnt['9'] + 1) // 2
num_cnt['9'] = 0

print(max(num_cnt.values()))