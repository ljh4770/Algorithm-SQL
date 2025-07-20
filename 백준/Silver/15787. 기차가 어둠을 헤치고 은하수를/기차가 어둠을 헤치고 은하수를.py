n, m = map(int, input().split())
insts = [tuple(map(int, input().split())) for _ in range(m)]

trains = [0] * n


for inst in insts:
    i, x = -1, -1
    if inst[0] in [1, 2]:
        # i: train num. x: seat num
        i, x = inst[1] - 1, inst[2] - 1
        if inst[0] == 1:
            trains[i] |= 1 << x
        else: # inst[0] == 2
            trains[i] &= ~(1 << x)
    else:
        i = inst[1] - 1 # i: train num
        if inst[0] == 3:
            trains[i] <<= 1
            trains[i] &= ~(1 << 20)
        else: # inst[0] == 4
            trains[i] >>= 1

print(len(set(trains)))