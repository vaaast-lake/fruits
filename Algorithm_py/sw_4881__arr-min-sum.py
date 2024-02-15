import sys

sys.stdin = open('sw_4881__arr-min-sum__input.txt', 'r')


def dfs(r=0, sum=0):
    global min_v
    if sum > min_v:
        return
    if r == N:
        min_v = sum
        return

    for c in range(N):
        if not board[c]:
            board[c] = table[r][c]
            dfs(r + 1, sum + table[r][c])
            board[c] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    min_v = 0xffff
    table = [list(map(int, input().split())) for _ in range(N)]
    board = [0] * N
    dfs()
    print(f'#{tc} {min_v}')

sys.stdin.close()