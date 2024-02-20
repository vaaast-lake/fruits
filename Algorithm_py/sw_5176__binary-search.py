import sys

sys.stdin = open('./sw_5176__binary-search__input.txt', 'r')

def in_order(root):
    global num

    if root:
        in_order(tree[root][0])
        lst[root] = num
        num += 1
        in_order(tree[root][1])

    # if root <= N:
    #     in_order(root*2)
    #     lst[root] = num
    #     num += 1
    #     in_order(root*2+1)


for tc in range(1, int(input())+1):
    N = int(input())
    num = 1
    lst = [None] * (N+1)
    tree = [0] + [[ None ] * 2 for _ in range(N+1)]
    for i in range(1, N+1):
        # if not tree[i//2][0]:
        #     tree[i//2][0] = i
        # else:
        #     tree[i//2][1] = i
        if i*2 <= N:
            tree[i][0] = i*2
        if i*2+1 <= N:
            tree[i][1] = i*2+1

    in_order(1)

    print(f'#{tc} {lst[1]} {lst[N//2]}')
    # print(tree)
    # print(lst)

sys.stdin.close()