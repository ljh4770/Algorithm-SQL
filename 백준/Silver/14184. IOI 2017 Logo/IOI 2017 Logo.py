import sys; input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    scores = dict()
    for _ in range(n):
        data = [*map(int, input().split())]
        k = data[0]
        picks = data[1:]

        if k >= 1:
            logo = picks[0]
            if logo not in scores: scores[logo] = [0, 0, 0]
            scores[logo][0] += 3
            scores[logo][1] += 1
        if k >= 2:
            logo = picks[1]
            if logo not in scores: scores[logo] = [0, 0, 0]
            scores[logo][0] += 2
            scores[logo][2] += 1
        if k >= 3:
            logo = picks[2]
            if logo not in scores: scores[logo] = [0, 0, 0]
            scores[logo][0] += 1
            
    max_stats = max(scores.values())
    winners = []
    for logo_id, stats in scores.items():
        if stats == max_stats:
            winners.append(logo_id)
    
    winners.sort()
    print(*winners)