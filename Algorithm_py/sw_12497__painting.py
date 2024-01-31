import sys

sys.stdin = open('./sw_12497__painting__input.txt', 'r')



# lst = list(range(2, 4))
# print(lst)

def paint(r1, c1, r2, c2, color):
    if color == 1:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if not (r_painted_area[r] & (1 << c)):
                    r_painted_area[r] |= 1 << c
    elif color == 2:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if not (b_painted_area[r] & (1 << c)):
                    b_painted_area[r] |= 1 << c


for ts in range(int(input())):

    r_painted_area = list(0 for _ in range(10))
    b_painted_area = list(0 for _ in range(10))

    painted_cnt = 0
    N = int(input())
    for i in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        paint(r1, c1, r2, c2, color)

    for r in range(10):
        for c in range(10):
            if (r_painted_area[r] & (1 << c)) and (b_painted_area[r] & (1 << c)):
                painted_cnt += 1

    print(f'#{ts+1} {painted_cnt}')


sys.stdin.close()

"""
0
0
0
0
0
0
0
0
0
0

2^9
추가는 |
확인은 &
"""