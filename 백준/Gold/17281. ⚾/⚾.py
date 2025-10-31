class Simulation:
    def __init__(self, player_order, results, n):
        self.player_order = player_order
        self.results = results
        self.cur_player_idx = 0
        
        self.N = n

    def play(self) -> int:
        total_score = 0
        
        # 총 N 이닝 (self.N은 이제 main에서 입력받은 n과 같음) 동안 경기를 진행
        for inning in range(self.N):
            # self.results[inning] : 이번 이닝의 선수별 결과 (길이 9)
            inning_score = self._run_inning(self.results[inning])
            total_score += inning_score
        
        return total_score

    def _run_inning(self, inning_results) -> int:
        outs = 0
        inning_score = 0
        # 1루, 2루, 3루 (0: 비어있음, 1: 주자 있음)
        bases = [0, 0, 0] 

        # 3아웃이 될 때까지 이닝 진행
        while outs < 3:
            # 1. 현재 타순(self.cur_player_idx)에 해당하는 선수의 ID
            current_player_id = self.player_order[self.cur_player_idx]
            
            # 2. 그 선수의 이번 이닝 결과 (0~4)
            result = inning_results[current_player_id]

            # 3. 결과 처리
            if result == 0: # 아웃
                outs += 1
            
            elif result == 1: # 안타
                # 주자 진루 (3루->2루->1루 순서로 처리해야 덮어쓰지 않음)
                if bases[2]: # 3루 주자
                    inning_score += 1 # 홈인
                    bases[2] = 0
                if bases[1]: # 2루 주자
                    bases[2] = 1 # 3루로
                    bases[1] = 0
                if bases[0]: # 1루 주자
                    bases[1] = 1 # 2루로
                    bases[0] = 0
                bases[0] = 1 # 타자 1루로
            
            elif result == 2: # 2루타
                if bases[2]: # 3루 주자
                    inning_score += 1 # 홈인
                    bases[2] = 0
                if bases[1]: # 2루 주자
                    inning_score += 1 # 홈인
                    bases[1] = 0
                if bases[0]: # 1루 주자
                    bases[2] = 1 # 3루로
                    bases[0] = 0
                bases[1] = 1 # 타자 2루로

            elif result == 3: # 3루타
                if bases[2]: # 3루 주자
                    inning_score += 1 # 홈인
                    bases[2] = 0
                if bases[1]: # 2루 주자
                    inning_score += 1 # 홈인
                    bases[1] = 0
                if bases[0]: # 1루 주자
                    inning_score += 1 # 홈인
                    bases[0] = 0
                bases[2] = 1 # 타자 3루로
            
            elif result == 4: # 홈런
                # 모든 주자 + 타자 홈인
                inning_score += (bases[0] + bases[1] + bases[2] + 1)
                bases = [0, 0, 0] # 모든 베이스 비움

            # 4. 다음 타자로 인덱스 변경 (타순은 0~8 반복)
            self.cur_player_idx = (self.cur_player_idx + 1) % 9
        
        # 3아웃, 이닝 종료
        return inning_score


def tracking():
    global n, results
    global player_order, visited, answer

    if len(player_order) == 9:
        sim = Simulation(player_order, results, n)
        score = sim.play()
        answer = max(answer, score)
        return
    elif len(player_order) == 3:
        player_order.append(0)
        tracking()
        player_order.pop()
        return

    for i in range(1, 9):
        if visited[i]:
            continue

        visited[i] = True
        player_order.append(i)
        tracking()
        player_order.pop()
        visited[i] = False
    

if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n = int(input())
    results = [[*map(int, input().split())] for _ in range(n)]

    player_order = []
    visited = [False] * 9
    answer = 0
    tracking()

    print(answer)