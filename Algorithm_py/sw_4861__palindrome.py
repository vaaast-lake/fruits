
import sys

sys.stdin = open('./sw_4861__palindrome__input.txt', 'r')

def find_palind(str_table):
    result = ''
    for i in range(N):
        for j in range(N - M + 1):
            if str_table[i][j] == str_table[i][j + M - 1]:
                for k in range(1, M // 2):
                    if str_table[i][j + k] != str_table[i][j + M - 1 - k]:
                        break
                else:
                    for n in range(M):
                        result += str_table[i][j+n]
                    return result
            if str_table[j][i] == str_table[j + M - 1][i]:
                for k in range(1, M // 2):
                    if str_table[j + k][i] != str_table[j + M - 1 - k][i]:
                        break
                else:
                    for n in range(M):
                        result += str_table[j+n][i]
                    return result


for ts in range(1, int(input())+1):
    N, M = map(int, input().split())

    table = [list(input()) for _ in range(N)]

    ans = find_palind(table)

    print(f'#{ts} {ans}')


sys.stdin.close()