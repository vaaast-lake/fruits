import sys

sys.stdin = open('./sw_1226__maze1__input.txt', 'r')

WALL = '1'
GOAL = '3'
SIZE = 16

def dfs(pos=(1, 1)):
    remote_ctr = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    cur_x, cur_y = pos

    if table[cur_x][cur_y] == GOAL:
        return 1

    for i in range(4):
        nx_x = cur_x + remote_ctr[i][0]
        nx_y = cur_y + remote_ctr[i][1]
        if table[nx_x][nx_y] != WALL and not visited[nx_x][nx_y] and\
                visited[nx_x][nx_y] < visited[cur_x][cur_y]:
            visited[nx_x][nx_y] = visited[cur_x][cur_y] + 1
            if dfs((nx_x, nx_y)):
                return 1

    return 0


for _ in range(1, 11):

    tc = int(input())
    table = [list(input()) for _ in range(SIZE)]
    visited = [[0]*SIZE for _ in range(SIZE)]
    visited[1][1] = 1

    result = dfs()

    print(f'#{tc} {result}')

sys.stdin.close()