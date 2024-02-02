import sys

sys.stdin = open('./sw_5789__box-changing__input.txt', 'r', encoding='UTF-8')

for ts in range(int(input())):

    N, Q = map(int, input().split())

    lst = [0]*N

    for i in range(1, Q+1):
        start, end = map(int, input().split())
        for j in range(start-1, end):
            lst[j] = i

    print(f'#{ts+1}', *lst)


sys.stdin.close()