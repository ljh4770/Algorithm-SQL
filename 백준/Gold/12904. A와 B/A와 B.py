s = [*input()]
t = [*input()]

while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    
    if s == t:
        print(1)
        break
else:
    print(0)