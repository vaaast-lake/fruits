import sys

sys.stdin = open('./sw_1240__simple-binary-password__input.txt', 'r')

dic = {
    13: 0,
    25: 1,
    19: 2,
    61: 3,
    35: 4,
    49: 5,
    47: 6,
    59: 7,
    55: 8,
    11: 9
}


def find_start_pos():
    for r in range(N - 1, -1, -1):
        for c in range(M - 1, -1, -1):
            if table[r][c]:
                return r, c


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    table = [list(map(int, list(input()))) for _ in range(N)]

    row, col = find_start_pos()

    even = odd = 0
    for cnt in range(8):

        num = 0
        for i in range(7):
            num |= table[row][col-i] << i

        if not cnt % 2:
            even += dic[num]
        else:
            odd += dic[num]

        col -= 7

    result = odd+even if not (odd*3+even) % 10 else 0

    print(f'#{tc} {result}')


sys.stdin.close()