from collections import Counter

eng_name = input()
char_cnt = Counter(eng_name)

left_result = ''
mid_result = ''
for i in range(65, 114 + 1, 1): # Iterate with alphabet (Upper Case Only)
    c = chr(i) # int to char
    cnt = char_cnt[c]

    # append to left-side result
    left_result += c * (cnt // 2)

    # append a char when the count value is odd
    if cnt % 2 == 1:
        mid_result += c
    
    # if there are multiple chars in mid_result, cannot form a palindrome
    if len(mid_result) > 1:
        print("I'm Sorry Hansoo")
        exit(0) # exit the process

# concatenate the result
print(left_result + mid_result + left_result[::-1])