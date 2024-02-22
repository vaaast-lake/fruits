import sys

sys.stdin = open('./bj_g5-5639__binary-searching-tree__input.txt', 'r')

input = sys.stdin.readlines
print = sys.stdout.write

NODE = 0
LEFT = 1
RIGHT = 2


def init_subtrees():
    sub_trees[0][NODE] = data[0]

    for i in range(1, data_len):
        sub_trees[i][NODE] = data[i]
        if data[i - 1] > data[i]:
            sub_trees[i - 1][LEFT] = data[i]
        elif data[i - 1] < data[i]:
            for j in range(i - 1, 0, -1):
                if j > 0 and data[j - 1] > data[i] and not sub_trees[j][RIGHT]:
                    sub_trees[j][RIGHT] = data[i]
                    break
            else:
                if data[0] < data[i] and not sub_trees[0][RIGHT]:
                    sub_trees[0][RIGHT] = data[i]
                else:
                    sub_trees[i-1][RIGHT] = data[i]



def post_order(root=0):
    if sub_trees[root][LEFT]:
        post_order(idx_dic[sub_trees[root][LEFT]])
    if sub_trees[root][RIGHT]:
        post_order(idx_dic[sub_trees[root][RIGHT]])
    print(f'{sub_trees[root][NODE]}\n')


data = list(map(lambda x: int(x.strip()), input()))
data_len = len(data)
idx_dic = {}
for i in range(data_len):
    idx_dic.setdefault(data[i], i)

sub_trees = [[None] * 3 for _ in range(data_len)]

init_subtrees()
post_order()


print(f'dic: {idx_dic}\n')
print(f'data: {data}\n')
print(f'sub_trees: {sub_trees}')



sys.stdin.close()