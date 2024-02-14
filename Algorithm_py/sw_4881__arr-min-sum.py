import sys

sys.stdin = open('sw_4881__arr-min-sum__input.txt', 'r')


def dfs(r=0, sum=0):
    global min_v
    if r == N and sum < min_v:
        min_v = sum
        return

    for c in range(N):
        if not board[c]:
            board[c] = table[r][c]
            dfs(r + 1, sum + table[r][c])


for tc in range(int(input())):
    N = int(input())
    miv_v = 0
    table = [list(map(int, input().split())) for _ in range(N)]
    board = [0] * N
    dfs()
    print(f'#{tc} {min_v}')

sys.stdin.close()