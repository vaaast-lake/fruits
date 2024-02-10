import sys

sys.stdin = open('./sw_2005__Pascal\'s-Triangle__input.txt', 'r')

for ts in range(1, int(input())+1):
    N = int(input())
    pasc = [[0]*n for n in range(1, N+1)]

    for i in range(N):
        for j in range(i+1):
            if j == 0:
                pasc[i][j] = 1
                continue
            if j == i:
                pasc[i][j] = 1
                break
            pasc[i][j] = pasc[i-1][j-1] + pasc[i-1][j]

    print(f'#{ts}')
    # for i in range(N):
    #     for j in range(i+1):
    #         print(pasc[i][j], end=' ')
    #     print()

    # print(pasc)
    for el in pasc:
        print(*el)

sys.stdin.close()