import sys

sys.stdin = open('./sw_5102__dist-from-node__input.txt', 'r')


def bfs(G):
    global rear
    global front

    front = (front + 1) % 60
    next_nd = queue[front]

    if next_nd == G:
        return visited[G]

    for n_nd in adj[next_nd]:
        if not visited[n_nd]:
            visited[n_nd] = visited[next_nd] + 1
            rear = (rear + 1) % 60
            queue[rear] = n_nd

    if rear == front:
        return 0

    return bfs(G)


for tc in range(1, int(input())+1):
    V, E = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))
    adj = [list() for _ in range(V+1)]

    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    queue = [None] * 60
    front = 0
    rear = 1
    visited = [0] * (V+1)

    queue[rear] = S
    result = bfs(G)

    print(f'#{tc} {result}')

sys.stdin.close()