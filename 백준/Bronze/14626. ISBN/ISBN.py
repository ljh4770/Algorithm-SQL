isbn = input()

sum_ = 0
weight = [1, 3]
missed_idx = -1

for i, d in enumerate(isbn):
    if d == '*':
        missed_idx = i        
    else:
        if i == 12:
            continue
        sum_ += int(d) * weight[i % 2]

if missed_idx == 12:
    print(10 - (sum_ % 10))
else:
    w = weight[missed_idx % 2]
    p = int(isbn[-1])
    for x in range(10):
        calc = (10 - (sum_ + w * x) % 10) % 10 
        if p == calc:
            print(x)
            break