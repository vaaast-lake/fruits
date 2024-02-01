import sys

sys.stdin = open('./sw_12507__binary-search__input.txt', 'r')

def binarySearch(target, l, r, dep = 1):
    if l > r:
        return False
    else:
        mid = (l + r) // 2
        if target == mid:
            return dep
        elif target < mid:
            return binarySearch(target, l, mid, dep=dep+1)
        elif target > mid:
            return binarySearch(target, mid, r, dep=dep+1)

for ts in range(int(input())):
    p, a, b = list(map(int, input().split()))
    a_cnt = binarySearch(a, 1, p)
    b_cnt = binarySearch(b, 1, p)

    result = 0
    if a_cnt < b_cnt:
        result = "A"
    elif a_cnt > b_cnt:
        result = "B"


    print(f'#{ts+1} {result}')


sys.stdin.close()