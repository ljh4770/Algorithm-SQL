def solution(players, m, k):
    history = []
    
    for player in players:
        total = sum((history + [1])[-k:]) * m

        if total > player:
            history = history + [0]
        else:
            add = (player - total) // m + 1
            history += [add]

    return sum(history)