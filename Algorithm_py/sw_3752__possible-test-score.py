import sys

sys.stdin = open('./sw_3752__possible-test-score__input.txt', 'r')


def comb(visit, cnt, idx=0, sum=0):
    global poss
    if cnt == N and not poss & 1 << sum:
        poss |= 1 << sum
        return

    if idx == N:
        return

    comb(visit, cnt+1, idx+1, sum+lst[idx])
    comb(visit, cnt, idx+1, sum)


for tc in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int, input().split()))
    visit = [False]*N
    poss = 0

    for i in range(N):
        comb(visit, i)

    cnt = 1
    bit = poss & -poss
    while bit:
        poss -= bit
        bit = poss & -poss
        cnt += 1

    print(f'#{tc} {cnt}')


sys.stdin.close()



# 2 2 3 5