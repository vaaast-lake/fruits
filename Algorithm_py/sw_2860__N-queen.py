import sys

sys.stdin = open('sw_2860__N-queen__input.txt', 'r')


def is_valid(c):
    for i in range(c):
        if board[c] == board[i] or c - i == abs(board[c]-board[i]):
            return False
    return True


def set_queen(c=0):
    if c == N:
        global cnt
        cnt += 1
        return

    for r in range(N):
        board[c] = r
        if is_valid(c):
            set_queen(c+1)


for tc in range(1, int(input())+1):
    N = int(input())
    board = [0]*N
    cnt = 0
    set_queen()

    print(f'#{tc} {cnt}')

sys.stdin.close()