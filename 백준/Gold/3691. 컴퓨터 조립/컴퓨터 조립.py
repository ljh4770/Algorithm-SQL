import sys; input = sys.stdin.readline

t = int(input()) # t : [1, 100]

for _ in range(t):
    # n : [1, 1000], budget : [1, 10 ** 9]
    n, budget = map(int, input().split())

    parts = dict() # store (price, quality) pair by type
    max_quality = 0
    for _ in range(n):
        # price : [0, 10 ** 6], quality : [1, 10 ** 9]
        type_, _, price, quality = input().rstrip().split()
        price, quality = int(price), int(quality)
        if type_ not in parts:
            parts[type_] = []
        parts[type_].append((price, quality))
        max_quality = max(max_quality, quality)

    for t, infos in parts.items():
        parts[t] = sorted(infos, key=lambda x: (x[0], -x[1]))

    # Binary Search for highest total quality wiht valid price
    # total quality - lowest quality of the type combination
    target = 0
    start, end = 0, max_quality
    while start <= end:
        mid = (start + end) // 2 # Inclusive Lower Bound of the total quality

        # Check if we can achieve total quality of mid
        total_price = 0 # with the budget
        continue_flag = False # continue for invalid mid
        for t, infos in parts.items(): # type, [(price, quality), ...]
            # Iterate to find type quality - appropriate quality for each type
            for p, q in infos:
                if q >= mid:
                    total_price += p
                    break
            else: # There not exist valid one with mid quality -> Too High mid
                end = mid - 1
                continue_flag = True
        
        if continue_flag:
            continue

        if total_price <= budget: # Valid combination
            target = mid
            start = mid + 1 # We might can increase the total quality
        else:
            end = mid - 1

    print(target)