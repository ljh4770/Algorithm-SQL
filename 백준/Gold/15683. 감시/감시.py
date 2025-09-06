def sort_cctvs(cctvs):
    type_cnt_dict = {i: [] for i in range(1, 6, 1)}
    for x, y, cctv_type in cctvs:
        type_cnt_dict[cctv_type].append((x, y, cctv_type))
    
    sorted_cctvs = []
    sorted_cctvs.extend(type_cnt_dict[5])
    sorted_cctvs.extend(type_cnt_dict[2])
    for i in [1, 3, 4]:
        sorted_cctvs.extend(type_cnt_dict[i])
    
    return sorted_cctvs

def mark_observable_cell(sx, sy, d):
    global n, m, office # mark observable cell as -1

    # parse passed direction
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dx, dy = directions[d]
    x, y = sx + dx, sy + dy

    marked_cells = [] # coords of marked cell
    cnt = 0 # observable cell count
    while True:
        if not (0 <= x < n and 0 <= y < m):
            break # out of bound
        cell = office[x][y]
        if cell == 6:
            break # wall
        elif 1 <= office[x][y] <= 5:
            pass
        elif office[x][y] == -1: # if -1, already observing
            pass
        else: # 0
            office[x][y] = -1
            marked_cells.append((x, y))
            cnt += 1
        x, y = x + dx, y + dy
    
    return marked_cells, cnt

def revert_observable_cell(cell_coords):
    global office

    for x, y in cell_coords:
        office[x][y] = 0

def tracking(k):
    global n, m, office
    global observable_cell_cnt, answer

    if k == cctv_cnt:
        answer_candidate = n * m - observable_cell_cnt - wall_cnt - cctv_cnt
        answer = min(answer, answer_candidate)
        return
    
    x, y, cctv_type = cctvs[k]
    marked_cells = []
    if cctv_type == 1: # rotate cctv for 4 directions
        for d in range(4):
            marked_cells, cnt = mark_observable_cell(x, y, d)
            observable_cell_cnt += cnt
            # print('-----' * k, cctv_type, marked_cells, cnt, observable_cell_cnt)
            tracking(k + 1)
            observable_cell_cnt -= cnt
            revert_observable_cell(marked_cells)
    elif cctv_type == 2: # rotate cctv for 2 directions
        for delta in [0, 1]:
            marked_cells = []
            local_cnt = 0
            for d in [0, 2]:
                d += delta
                coords, cnt = mark_observable_cell(x, y, d)
                marked_cells.extend(coords)
                local_cnt += cnt
            observable_cell_cnt += local_cnt
            # print('-----' * k, cctv_type, marked_cells, local_cnt, observable_cell_cnt)
            tracking(k + 1)
            observable_cell_cnt -= local_cnt
            revert_observable_cell(marked_cells)
    elif cctv_type == 3: # rotate cctv for 4 directions
        for d1, d2 in [(0, 1), (1, 2), (2, 3), (3, 0)]:
            marked_cells = []
            local_cnt = 0
            for d in [d1, d2]:
                coords, cnt = mark_observable_cell(x, y, d)
                marked_cells.extend(coords)
                local_cnt += cnt
            observable_cell_cnt += local_cnt
            # print('-----' * k, cctv_type, marked_cells, local_cnt, observable_cell_cnt)
            tracking(k + 1)
            observable_cell_cnt -= local_cnt
            revert_observable_cell(marked_cells)
    elif cctv_type == 4: # rotate cctv for 4 directions
        for i in range(4): # direction s.t. cannot observe
            marked_cells = []
            local_cnt = 0
            for d in range(4):
                if i == d:
                    continue
                coords, cnt = mark_observable_cell(x, y, d)
                marked_cells.extend(coords)
                local_cnt += cnt
            observable_cell_cnt += local_cnt
            # print('-----' * k, cctv_type, marked_cells, local_cnt, observable_cell_cnt)
            tracking(k + 1)
            observable_cell_cnt -= local_cnt
            revert_observable_cell(marked_cells)
    elif cctv_type == 5: # do not rotate cctv
        marked_cells = []
        local_cnt = 0
        for d in range(4):
            coords, cnt = mark_observable_cell(x, y, d)
            marked_cells.extend(coords)
            local_cnt += cnt
        observable_cell_cnt += local_cnt
        # print('-----' * k, cctv_type, marked_cells, local_cnt, observable_cell_cnt)
        tracking(k + 1)
        observable_cell_cnt -= local_cnt
        revert_observable_cell(marked_cells)
    

if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n, m = map(int, input().split()) # n, m : [1, 8]
    office = [list(map(int, input().split())) for _ in range(n)]
    cctvs = [] # coords of cctvs & type - (x, y, type)
    wall_cnt = 0
    cctv_cnt = 0
    for i in range(n):
        for j in range(m):
            if 1 <= office[i][j] <= 5:
                cctvs.append((i, j, office[i][j]))
                cctv_cnt += 1
            if office[i][j] == 6:
                wall_cnt += 1

    cctvs = sort_cctvs(cctvs) # sort order - 5, 2, 1, 3, 4
    cctv_cnt = len(cctvs)
    observable_cell_cnt = 0
    answer = float('inf')
    tracking(0)

    print(answer)