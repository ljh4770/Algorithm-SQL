import sys; input = sys.stdin.readline
from collections import Counter

N = int(input())
books = [input().rstrip() for _ in range(N)]

book_cnt = Counter(books)
best_sellers = sorted(book_cnt.items(), key=lambda x: (-x[1], x[0]))
print(best_sellers[0][0])
