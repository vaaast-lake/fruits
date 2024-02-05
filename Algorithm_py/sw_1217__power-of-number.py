import sys

sys.stdin = open('./sw_1217__power-of-number__input.txt', 'r')

def r_f(num, power, cumul_num=1):

    if power == 0:
        return cumul_num

    return r_f(num, power-1, cumul_num * num)


for _ in range(1, 11):

    tc = int(input())
    N, M = map(int, input().split())

    result = r_f(N, M)

    print(f'#{tc} {result}')



sys.stdin.close()