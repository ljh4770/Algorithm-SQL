def sum_term(term):
    nums = term.split('+')
    res = 0
    for num in nums:
        res += int(num)

    return res

import sys

exp = sys.stdin.readline().strip()
exp = exp.split('-')
first_flag = True
res = 0

for term in exp: # term은 +와 숫자만 포함
    s = sum_term(term)
    if first_flag == True:
        first_flag = False
        res += s
    else:
        res -= s

print(res)