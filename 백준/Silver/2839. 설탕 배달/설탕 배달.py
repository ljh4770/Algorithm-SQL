N = int(input())

q, r = divmod(N, 5)

# p, s = divmod(r, 3)

# if s !=0:
#     print(-1)
# else:
#     print(q+p)

flag = True

if r == 0:
    pass

elif r == 1:
    if q < 1:
        flag = False
    else:
        q += 1

elif r == 2:
    if q < 2:
        flag = False
    else:
        q += 2
    
elif r == 3:
    q += 1

elif r == 4:
    if q < 1:
        flag = False
    else:
        q += 2

if flag == True:
    print(q)
else:
    print(-1)

