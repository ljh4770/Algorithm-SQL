a, b = map(int, input().split())

cards = [i for i in range(1, 10 + 1)] + [i for i in range(1, 10 + 1)]

cards.remove(a)
cards.remove(b)

is_ttang = True if a == b else False

score_me = a if is_ttang else (a + b) % 10

win = 0
draw = 0
lose = 0

for i in range(17):
    x = cards[i]
    for j in range(i + 1, 18):
        y = cards[j]
        is_ggut = True if x != y else False

        # both ttang
        if is_ttang and not is_ggut:
            if score_me > x:
                win += 1
            elif score_me == x:
                draw += 1
            else:
                lose += 1
        # me ttang & enemy ggut -> always win
        elif is_ttang and is_ggut:
            win += 1
        # me ggut & enemy ttang -> always lose
        elif not is_ttang and not is_ggut:
            lose += 1
        # both ggut
        elif not is_ttang and is_ggut:
            score_enemy = (x + y) % 10
            if score_me > score_enemy:
                win += 1
            elif score_me == score_enemy:
                draw += 1
            else:
                lose += 1
                
n = win + draw + lose
print(f"{win / n:.3f}")