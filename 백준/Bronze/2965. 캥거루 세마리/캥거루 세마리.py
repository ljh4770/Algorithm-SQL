# a,b,c = map(int, input().split())
# # a,b,c=3,5,9

def dh(a, b, c):
    count = 0

    while True:
        equ1 = b-a-1
        equ2 = c-b-1

        if (equ1==0) and (equ2==0):   # 더이상점프안되는경우
            break
        
        elif equ1 <= equ2:  # 같은 경우 고려해서 <=
            a,b,c = b,b+1,c
            count +=1
            
        elif equ1 > equ2:
            a,b,c = a,b-1,b
            count +=1

    # print(count)
    return count

# --------------- 밑에는 블로그
# while 1:
#     try:
#         A, B, C = map(int, input().split())
#         print(max(B-A, C-B)-1)
#     except:
#         break
    

def gpt(a, b, c):
    # print(max(b - a - 1, c - b - 1))
    return max(b - a - 1, c - b - 1)

if __name__ == '__main__':
    # for a in range(1, 98, 1):
    #     for b in range(a + 1, 99, 1):
    #         for c in range(b + 1, 100, 1):
    #             d = dh(a, b, c)
    #             g = gpt(a, b, c)
    #             if d == g:
    #                 print(f"DH: {d}\t GPT: {g} --- a: {a}, b: {b}, c: {c}")
    #             else:
    #                 print(f"DH: {d}\t GPT: {g} --- a: {a}, b: {b}, c: {c}")    
    a,b,c = map(int, input().split())
    answer = dh(a, b, c)
    print(answer)