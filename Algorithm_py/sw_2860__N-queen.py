import sys

sys.stdin = open('sw_2860__N-queen__input.txt', 'r')


# def is_valid(c):
#     for i in range(c):
#         if board[c] == board[i] or c - i == abs(board[c]-board[i]):
#             return False
#     return True
#
#
# def set_queen(c=0):
#     if c == N:
#         global cnt
#         cnt += 1
#         return
#
#     for r in range(N):
#         board[c] = r
#         if is_valid(c):
#             set_queen(c+1)


def cnt_n_queen(ld=0, col=0, rd=0, is_first=True):
    global cnt
    if col == done:
        cnt += 1
        return

    poss = ~(ld | rd | col)
    while poss & done:
        bit = poss & -poss
        if is_first and half == bit:
            cnt *= 2
            if is_pair: break
        if is_first and half < bit:
            break
        poss -= bit
        cnt_n_queen((ld | bit) << 1, col | bit, (rd | bit) >> 1, False)


for tc in range(1, int(input())+1):
    N = int(input())
    # board = [0]*N
    cnt = 0
    done = (1 << N) - 1
    is_pair = N % 2 == 0
    half = 1 << N // 2 if is_pair else 1 << ((N-1) // 2)
    # set_queen()
    cnt_n_queen()

    print(f'#{tc} {cnt}')

sys.stdin.close()