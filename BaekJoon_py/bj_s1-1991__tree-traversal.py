import sys

sys.stdin = open('./bj_s1-1991__tree-traversal__input.txt', 'r')

input = sys.stdin.readline
print = sys.stdout.write

NODE = 0
LEFT = 1
RIGHT = 2


def in_order(root=1, idx=1):
    pass


def pre_order(root=1, idx=1):
    if root <= N:
        tree[root] = data[idx][NODE]
        print(f'{tree[root]}')
        if data[idx][LEFT] != '.':
            left_idx = dic[data[idx][LEFT]]
            pre_order(root * 2, left_idx)
        if root * 2 + 1 <= N and data[idx][RIGHT] != '.':
            right_idx = dic[data[idx][RIGHT]]
            pre_order(root * 2 + 1, right_idx)


def post_order(root=1):
    pass


N = int(input())
data = [None] + [input().split() for _ in range(N)]
tree = [None] * (2 ** N)

dic = {}

for i in range(1, N+1):
    dic.setdefault(data[i][NODE], i)

pre_order()

print(f'data: {data}\n')
print(f'dic: {dic}\n')
print(f'tree: {tree}')


sys.stdin.close()