if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n, m = map(int, input().split())
    cards = [*map(int, input().split())]
    cards.sort()


    if n == 2:
        res =  sum(cards) * (2 ** m)
        print(res)
        exit(0)

    for _ in range(m):
        if cards[1] > cards[2]:
            cards.sort()
        
        x, y = cards[0], cards[1]
        cards[0], cards[1] = x + y, x + y

    print(sum(cards))