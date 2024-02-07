import sys

sys.stdin = open('./sw_2005__Pascal\'s-Triangle__input.txt', 'r')

for ts in range(1, int(input())+1):
    N = int(input())
    pasc = [[0]*N for _ in range(N)]
    pasc[0][0] = 1

    for i in range(1, N):
        for j in range(i+1):
            if j == i:
                pasc[i][j] = 1
            pasc[i][j] = pasc[i-1][j-1] + pasc[i-1][j]

    print(f'#{ts}')
    for i in range(N):
        for j in range(i+1):
            print(pasc[i][j], end=' ')
        print()

sys.stdin.close()