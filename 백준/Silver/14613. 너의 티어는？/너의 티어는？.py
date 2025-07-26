from math import factorial as fact

def multivariate(win, lose, draw, w, l, d):
    numerator = fact(20) * (w ** win) * (l ** lose) * (d ** draw)
    denominator = fact(win) * fact(lose) * fact(draw)
    return numerator / denominator


if __name__ == "__main__":
    w, l, d = map(float, input().split())

    probs = [0] * 5
    for win in range(0, 21, 1):
        for lose in range(0, 21 - win, 1):
            points = 2000 + 50 * (win - lose)
            draw = 20 - win - lose
            p = multivariate(win, lose, draw, w, l, d)
            if points < 1500:
                probs[0] += p
            elif points < 2000:
                probs[1] += p
            elif points < 2500:
                probs[2] += p
            elif points < 3000:
                probs[3] += p
            else:
                probs[4] += p
    for p in probs:
        print(f"{p:.8f}")