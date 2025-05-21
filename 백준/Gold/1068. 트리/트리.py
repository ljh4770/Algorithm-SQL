import sys
sys.setrecursionlimit(10**7)  # 혹시 모를 깊은 재귀 대비
input = sys.stdin.readline

n = int(input().strip())
parents = list(map(int, input().split()))
del_node = int(input().rstrip())

# 자식 리스트
tree = [[] for _ in range(n)]
root = -1

for node, par in enumerate(parents):
    if par == -1:
        root = node
    else:
        tree[par].append(node)

# 만약 제거 노드가 루트이면 => 전체가 사라지므로 답은 0
if del_node == root:
    print(0)
    sys.exit(0)

# ------------------------------
# (1) 서브 트리 제거 DFS
# ------------------------------
def remove_subtree(cur, par):
    """
    부모 par의 자식 목록에서 cur 제거 후,
    cur의 자식들에 대해서도 재귀적으로 부모-자식 연결을 끊는다.
    """
    # 부모가 -1이 아니면(즉, 실제 유효한 부모가 있으면) 부모의 자식 목록에서 cur 제거
    if par != -1:
        tree[par].remove(cur)
    
    # cur가 가진 자식들에 대해서도 동일 작업 반복
    for child in tree[cur]:
        remove_subtree(child, cur)

# del_node의 부모를 찾아서 remove_subtree 호출
del_par = parents[del_node]
remove_subtree(del_node, del_par)

# ------------------------------
# (2) 남은 트리에서 리프 개수 DFS
# ------------------------------
def count_leaves_dfs(cur):
    """
    남아 있는 트리에서, 자식이 없으면 리프이다.
    """
    # 자식이 없으면 리프
    if not tree[cur]:
        return 1
    
    total_leaf = 0
    for child in tree[cur]:
        total_leaf += count_leaves_dfs(child)
    return total_leaf

answer = count_leaves_dfs(root)
print(answer)