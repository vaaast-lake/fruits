import sys

sys.stdin = open('sw_1220__magnatic__input.txt', 'r')


for ts in range(1, 11):

    table_size = int(input())

    table = [input().split() for _ in range(table_size)]

    cnt = 0
    for i in range(table_size):
        for j in range(table_size):
            if table[i][j] == '1':
                k = i+1
                while k < table_size:
                    if table[k][j] == '2':
                        cnt += 1
                        break
                    elif table[k][j] == '1':
                        break
                    k += 1

    print(f'#{ts} {cnt}')


sys.stdin.close()