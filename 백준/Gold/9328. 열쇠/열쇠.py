from collections import deque


def bfs(space, h, w, keys):
    q = deque()
    q.append((0, 0))
    visited = [[False] * (w + 2) for _ in range(h + 2)] # padding for walls
    visited[0][0] = True

    # to keep track of visited documents
    visited_docs = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    cnt = 0
    while q:
        r, c = q.popleft()

        for dx, dy in directions:
            nr, nc = r + dx, c + dy

            # Continue for the following conditions:
            if (not (0 <= nr < h + 2 and 0 <= nc < w + 2) # out of bounds
                or space[nr][nc] == '*'                   # wall
                or visited[nr][nc] == True):              # already visited
                continue
            
            ch = space[nr][nc]
            # door
            if 'A' <= ch <= 'Z':
                # if the key for this door is not available
                if keys[chr(ord(ch) + 32)] == False:
                    continue
            # key
            elif 'a' <= ch <= 'z':
                if keys[ch] == False:
                    keys[ch] = True
                    # reset visited
                    visited = [[False] * (w + 2) for _ in range(h + 2)]
            # docs and not visited
            elif ch == '$' and (nr, nc) not in visited_docs:
                cnt += 1
                visited_docs.append((nr, nc))
            
            visited[nr][nc] = True
            q.append((nr, nc))

    return cnt


def solve():
    # h: height, w: width of the space
    h, w = map(int, input().split(' '))
    # Building space represented as a 2D grid
    space = [list('.' + input().rstrip() + '.') for _ in range(h)]
    space = [['.'] * (w + 2)] + space + [['.'] * (w + 2)]  # padding for walls
    # .: empty space, *: wall, $: docs, Upper Case: door, Lower Case: key
    keys = dict() # keys: keys available, if "0" no keys
    for c in range(26):
        keys[chr(c + ord('a'))] = False
    for c in input().rstrip():
        if c.isalpha():
            keys[c] = True

    answer = bfs(space, h, w, keys)
    print(answer)


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        solve()