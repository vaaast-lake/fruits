import sys

sys.stdin = open('./sw_6485__bus-line-of-samsung__input.txt', 'r', encoding='UTF-8')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = [0]*5001 #. 5000번 정류장까지 표시
    #. N개의 노선을 정류장에 표시
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1): #. A <= B
            cnt[j] += 1

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]

    print(f'#{tc}', end=' ')

    for i in bus_stop:
        print(cnt[i], end = ' ')

    print()

sys.stdin.close()