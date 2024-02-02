import sys

sys.stdin = open('./sw_1216__palindrome2__input.txt', 'r', encoding='UTF-8')


# def find_max_p_len(r, c, p_len):
#     if max_v > p_len:
#         return 0
#     max_c = 0
#     if c + p_len < 100 and 100 - c > max_v:
#         cnt_c = 0
#         for i in range(p_len // 2):
#             if str_table[r][c + i] == str_table[r][c + p_len-1 - i]:
#                 cnt_c += 1
#             else:
#                 break
#             if cnt_c == p_len // 2 and max_c < p_len:
#                 max_c = p_len
#                 break
#     max_r = 0
#     if r + p_len < 100 and 100 - r > max_v:
#         cnt_r = 0
#         for i in range(p_len // 2):
#             if str_table[r + i][c] == str_table[r + p_len-1 - i][c]:
#                 cnt_r += 1
#             else:
#                 break
#             if cnt_r == p_len // 2 and max_r < p_len:
#                 max_r = p_len
#                 break
#
#     return max_c if max_c > max_r else max_r
#
#
# for _ in range(1, 11):
#     tc = int(input())
#
#     str_table = []
#     for _ in range(100):
#         str_table.append(list(input()))
#
#
#     max_v = 1
#     for r in range(100):
#         for c in range(100):
#             for p_len in range(99, 1, -1):
#                 find_v = find_max_p_len(r, c, p_len)
#                 if find_v > max_v:
#                     max_v = find_v
#                     # if tc == 5:
#                         # print(f'#{tc}, r: {r}, c: {c}, find_v: {find_v}')
#
#     print(f'#{tc} {max_v}')

for tc in range(10):
    test_case = int(input())
    board = [list(input()) for _ in range(100)]
    turn_board = [list(tuple) for tuple in zip(*board)]
    max_length = 0

    for N in range(1, 25):
        for row in board:
            for col in range(101 - N):
                rvs = row[col:col + N]
                rvs.reverse()
                if row[col:col + N] == rvs:
                    if tc == 5:
                        print(f'#{tc}, arr:{row[col:col+N]}, r:{col}, c:{col+N}')
                    max_length = len(rvs)
        for row in turn_board:
            for col in range(101 - N):
                rvs = row[col:col + N]
                rvs.reverse()
                if row[col:col + N] == rvs:
                    max_length = len(rvs)

#. [9][82] 에 있는 거 못 찾음.

    # print(f'#{test_case} {max_length}')

sys.stdin.close()