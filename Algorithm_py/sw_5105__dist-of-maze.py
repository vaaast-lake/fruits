import sys

# sys.stdin = open('./sw_5105__dist-of-maze__input.txt', 'r')

WALL = '1'
START = '2'
GOAL = '3'
PATH = '0'
MOD = 100000

def find_pos():
    s_x = s_y = g_x = g_y = cnt = 0

    for i in range(N):
        for j in range(N):
            if table[i][j] == START:
                s_x = i
                s_y = j
                cnt += 1
            if table[i][j] == GOAL:
                g_x = i
                g_y = j
                cnt += 1
            if cnt == 2:
                return s_x, s_y, g_x, g_y

def bfs(queue):
    global front
    global rear

    if front == rear:
        return 0

    front = (front + 1) % MOD
    cur_nd = queue[front]

    if table[cur_nd[0]][cur_nd[1]] == GOAL:
        return visited[cur_nd[0]][cur_nd[1]] - 2

    for i in range(4):
        nx_nd_x = cur_nd[0] + remote_ctr[i][0]
        nx_nd_y = cur_nd[1] + remote_ctr[i][1]
        if -1 < nx_nd_x < N and -1 < nx_nd_y < N and \
                table[nx_nd_x][nx_nd_y] != WALL and not visited[nx_nd_x][nx_nd_y]:
            visited[nx_nd_x][nx_nd_y] = visited[cur_nd[0]][cur_nd[1]] + 1
            rear = (rear + 1) % MOD
            queue[rear] = [nx_nd_x, nx_nd_y]

    return bfs(queue)


for tc in range(1, int(input())+1):
    N = int(input())
    table = [list(input()) for _ in range(N)]

    s_x, s_y, g_x, g_y = find_pos()

    remote_ctr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[0] * N for _ in range(N)]

    queue = [None] * MOD
    front = 0
    rear = 1
    queue[rear] = [s_x, s_y]
    visited[s_x][s_y] = 1
    result = bfs(queue)

    print(f'#{tc} {result}')


sys.stdin.close()

# 1
# 5
# 13021
# 11101
# 10001
# 10111
# 10001