import sys

sys.stdin = open('./sw_1231__in_order-traversal__input.txt', 'r')

def in_order(root):
    global string
    if root <= N:
        in_order(root*2)
        # print(data[root][1], end='')
        string += data[root][1]
        in_order(root*2+1)



for tc in range(1, 11):
    N = int(input())
    data = [0] + [input().split() for _ in range(N)]
    string = ''
    # strings = [0] * (N+1)
    # for i in range(1, N+1):
    #     strings[i] = data[i-1][1]

    in_order(1)
    print(f'#{tc} {string}')


sys.stdin.close()