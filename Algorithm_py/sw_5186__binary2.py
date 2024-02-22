import sys

sys.stdin = open('./sw_5186__binary2__input.txt', 'r')


for tc in range(1, int(input())+1):

    N = float(input())

    result = ''
    while N:
        N = N * 2
        if N >= 1:
            N -= 1
            result += '1'
        else:
            result += '0'

        if len(result) > 12:
            result = 'overflow'
            break

    print(f'#{tc} {result}')


sys.stdin.close()