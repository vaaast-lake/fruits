import sys

sys.stdin = open('./sw_4871__graph-edge__input.txt', 'r')

def dfs(edges, target, node):
    if node == target:
        return 1

    visit[node] = True
    for next_nd in edges[node]:
        if not visit[next_nd] \
                and dfs(edges, target, next_nd):
            return 1

    return 0

for ts in range(1, int(input())+1):
    V, E = list(map(int, input().split()))

    edges = [list() for _ in range(V+1)]
    visit = [False for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = list(map(int, input().split()))
        edges[v1].append(v2)

    S, G = list(map(int, input().split()))

    result = dfs(edges, G, S)

    print(f'#{ts} {result}')

sys.stdin.close()