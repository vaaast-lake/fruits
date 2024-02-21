import sys

sys.stdin = open('./sw_5177__binary-heap__input.txt', 'r')

def heap_init(val):
    global heap_cnt
    heap_cnt += 1
    heap[heap_cnt] = val

    child = heap_cnt
    parent = heap_cnt // 2
    while parent > 0 and heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        child = parent
        parent = child // 2


for tc in range(1, int(input())+1):

    N = int(input())
    data = list(map(int, input().split()))
    heap_cnt = 0
    heap = [None] * (N+1)

    for el in data:
        heap_init(el)

    tmp_cnt = heap_cnt // 2
    result = 0
    while tmp_cnt > 0:
        result += heap[tmp_cnt]
        tmp_cnt //= 2

    print(f'#{tc} {result}')

sys.stdin.close()