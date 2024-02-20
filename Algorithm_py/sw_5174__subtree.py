import sys

sys.stdin = open('./sw_5174__subtree__input.txt', 'r')

def find_child(root):
    cnt = 1
    q = [root]
    while q:
        node = q.pop(0)
        for el in tree[node]:
            if el:
                q.append(el)
                cnt += 1

    return cnt


for tc in range(1, int(input())+1):
    edges, root = list(map(int, input().split()))
    data = list(map(int, input().split()))
    tree = [[None] * 2 for _ in range(edges+2)]

    for i in range(0, edges*2, 2):
        if not tree[data[i]][0]:
            tree[data[i]][0] = data[i+1]
        else:
            tree[data[i]][1] = data[i+1]

    print(f'#{tc} {find_child(root)}')


sys.stdin.close()