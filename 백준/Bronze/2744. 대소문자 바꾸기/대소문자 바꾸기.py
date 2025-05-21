import sys
input = sys.stdin.readline

string = input().rstrip()
answer = ''

a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')

for c in string:
    ascii = ord(c)
    if a <= ascii <= z:
        answer += chr(ascii - 32)
    else:
        answer += chr(ascii + 32)
print(answer)