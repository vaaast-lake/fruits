import sys

sys.stdin = open('./sw_5176__binary-search__input.txt', 'r')

def in_order(root):
    global num

    if root:
        in_order(tree[root][0])
        lst[root] = num
        num += 1
        in_order(tree[root][1])


for tc in range(1, int(input())+1):
    N = int(input())
    num = 1
    lst = [0] * (N+1)
    tree = [0] + [[ None ] * 2 for _ in range(N+1)]
    for i in range(1, N+1):
        if i == 1:
            continue
        if not tree[i//2][0]:
            tree[i//2][0] = i
        else:
            tree[i//2][1] = i

    in_order(1)

    print(f'#{tc} {lst[1]} {lst[N//2]}')
    # print(tree)

sys.stdin.close()