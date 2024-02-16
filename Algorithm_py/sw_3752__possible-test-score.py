import sys

sys.stdin = open('./sw_3752__possible-test-score__input.txt', 'r')


def comb(i, cnt=0, idx=0, sum=0):
    global poss

    if idx == N:
        return

    if cnt == i:
        poss |= 1 << sum
        board[idx] |= poss
        return

    comb(i, cnt+1, idx+1, sum+lst[idx])
    if not board[idx+1] & 1 << sum:
        comb(i, cnt, idx+1, sum)


for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    poss = 0
    board = [0] * (N+1)

    for i in range(N):
        comb(i)

    result_cnt = 1
    bit = poss & -poss
    while bit:
        poss -= bit
        bit = poss & -poss
        result_cnt += 1

    print(f'#{tc} {result_cnt}')

sys.stdin.close()



