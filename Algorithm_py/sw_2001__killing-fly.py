import sys

sys.stdin = open('./sw_2001__killing-fly__input.txt', 'r')

for ts in range(int(input())):
    N, M = map(int, input().split())

    table = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        table.append(tmp)
    max_v = 0
    for r in range(N):
        for c in range(N):
            tmp_v = 0
            if r + M - 1 > N - 1 or c + M - 1 > N - 1:
                continue
            for ri in range(M):
                for cj in range(M):
                    tmp_v += table[r+ri][c+cj]
            if max_v < tmp_v:
                max_v = tmp_v

    print(f'#{ts+1} {max_v}')





sys.stdin.close()