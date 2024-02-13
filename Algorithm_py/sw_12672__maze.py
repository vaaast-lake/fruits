import sys

sys.stdin = open('sw_12672__maze__input.txt', 'r')

START = '2'
DEST = '3'
WALL = '1'
remote_ctr = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def find_exit_dfs(cur_x, cur_y, table, visit, N):
    if table[cur_x][cur_y] == DEST:
        return 1

    visit[cur_x][cur_y] = True
    for i in range(4):
        mv_x, mv_y = remote_ctr[i]
        nx_x, nx_y = cur_x + mv_x, cur_y + mv_y

        if -1 < nx_x < N and -1 < nx_y < N and \
                not visit[nx_x][nx_y] and table[nx_x][nx_y] != WALL:
            if find_exit_dfs(nx_x, nx_y, table, visit, N):
                return 1

    return 0

def find_start_pos(table):
    for i in range(N):
        for j in range(N):
            if table[i][j] == START:
                return (i, j)
    return False

for ts in range(1, int(input())+1):

    N = int(input())
    table = [list(input()) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]

    pos_x, pos_y = find_start_pos(table)

    result = find_exit_dfs(pos_x, pos_y, table, visit, N)

    print(f'#{ts} {result}')


sys.stdin.close()