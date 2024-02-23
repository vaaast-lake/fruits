import sys

# sys.stdin = open('./bj_g5-5639__binary-searching-tree__input.txt', 'r')

input = sys.stdin.readlines
print = sys.stdout.write
sys.setrecursionlimit(20000)


def post_order_div_conquer(left, right):
    if left > right:
        return

    mid = right+1 #. 더 큰 수가 없을 때 base case로 만들어 주기 위해 right+1로 초기화
    for i in range(left+1, right+1):
        if data[left] < data[i]:
            mid = i
            break

    post_order_div_conquer(left+1, mid-1)
    post_order_div_conquer(mid, right)
    print(f'{data[left]}\n')


data = list(map(lambda x: int(x.strip()), input()))
data_len = len(data)

# print(f'data: {data}\n')

post_order_div_conquer(0, data_len-1) #. 실제 인덱스 번호를 기준으로 돌기 위해 인덱스 범위 내의 번호를 넣어줌

sys.stdin.close()