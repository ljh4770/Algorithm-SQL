word = input()
arr = [word[i:] for i in range(len(word))]
arr.sort()

for suffix in arr:
    print(suffix)