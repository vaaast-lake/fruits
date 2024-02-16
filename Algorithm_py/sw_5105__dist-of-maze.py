import sys

sys.stdin = open('./sw_5105__dist-of-maze__input.txt', 'r')

WALL = '1'
START = '2'
GOAL = '3'
MOD = 100000


def find_pos():
    for i in range(N+2):
        for j in range(N+2):
            if table[i][j] == START:
                return i, j


# bfs를 재귀로 돌면, 모든 좌표를 도는 경우 스택 탈출하는 경우 없이 시스템 스택을 쌓아갈 수 있다.
# 최악의 경우 모든 좌표를 시스템 스택에 쌓으며 탐색하는 셈.
# def bfs(queue):
#     global front
#     global rear
#
#     if front == rear:
#         return 0
#
#     front = (front + 1) % MOD
#     cur_nd = queue[front]
#
#     if table[cur_nd[0]][cur_nd[1]] == GOAL:
#         return visited[cur_nd[0]][cur_nd[1]] - 2
#
#     for i in range(4):
#         nx_nd_x = cur_nd[0] + remote_ctr[i][0]
#         nx_nd_y = cur_nd[1] + remote_ctr[i][1]
#         if table[nx_nd_x][nx_nd_y] != WALL and not visited[nx_nd_x][nx_nd_y]:
#             visited[nx_nd_x][nx_nd_y] = visited[cur_nd[0]][cur_nd[1]] + 1
#             rear = (rear + 1) % MOD
#             queue[rear] = [nx_nd_x, nx_nd_y]
#
#     return bfs(queue)

def bfs():
    queue = [None] * MOD
    front = 0
    rear = 1
    remote_ctr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    queue[rear] = find_pos()

    while front != rear:
        front = (front + 1) % MOD
        cur_x, cur_y = queue[front]
        if table[cur_x][cur_y] == GOAL:
            return visited[cur_x][cur_y] - 1
        for i in range(4):
            nx_x, nx_y = cur_x + remote_ctr[i][0], cur_y + remote_ctr[i][1]
            if not visited[nx_x][nx_y] and table[nx_x][nx_y] != WALL:
                visited[nx_x][nx_y] = visited[cur_x][cur_y] + 1
                rear = (rear + 1) % MOD
                queue[rear] = nx_x, nx_y
    return 0


for tc in range(1, int(input())+1):
    N = int(input())
    table = [['1'] * (N+2)]
    table += [['1'] + list(input()) + ['1'] for _ in range(N)]
    table += [['1'] * (N+2)]

    # result = bfs(queue)
    result = bfs()

    print(f'#{tc} {result}')

sys.stdin.close()

