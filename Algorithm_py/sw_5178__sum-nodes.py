import sys

sys.stdin = open('./sw_5178__sum-nodes__input.txt', 'r')

'''
[None, None, None, None, None, None, 501, 170, 42, 468, 335]
'''

def post_order(root=1):
    if root * 2 <= N and not heap[root]:
        num1 = post_order(root * 2)
        num2 = post_order(root * 2 + 1) if root * 2 + 1 <= N else 0
        heap[root] = num1 + num2

        #. num2 = post_order(root * 2 + 1) if root * 2 + 1 <= N else None
        #. if num1 and num2:
        #.     heap[root] = num1 + num2
        #. else:
        #.     heap[root] = num1 if num1 else num2

    return heap[root]


for tc in range(1, int(input())+1):

    N, leaf_N, result_nd = map(int, input().split())

    heap = [None] * (N+1)
    for _ in range(leaf_N):
        node_n, num = map(int, input().split())
        heap[node_n] = num

    heap_cnt = 0
    if heap[result_nd]:
        print(f'#{tc} {heap[result_nd]}')
    else:
        post_order()
        print(f'#{tc} {heap[result_nd]}')



sys.stdin.close()