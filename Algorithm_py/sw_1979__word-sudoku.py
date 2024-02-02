import sys

sys.stdin = open('./sw_1979__word-sudoku__input.txt', 'r', encoding='UTF-8')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    #. 가장 오른쪽 열에 0을 더하고, 마지막 행에 0을 추가하는 방식
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    N += 1 #. 0인 열/행 추가

    #. 가로, 세로로 연속한 1의 개수가 k인 경우를
    ans = 0
    for i in range(N):
        cnt = 0 #. i 행에서 연속한 1의 개수
        for j in range(N):
            if arr[i][j]:
                cnt+=1
            else: #. arr[i][j] == 0
                if cnt == K:
                    ans += 1
                cnt = 0

    for j in range(N):
        cnt = 0 #. j 열에서 연속한 1의 개수
        for i in range(N):
            if arr[i][j]:
                cnt+=1
            else: #. arr[j][i] == 0
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f'#{tc} {ans}')



sys.stdin.close()