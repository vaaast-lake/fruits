import sys

sys.stdin = open('./sw_1215__palindrome__input.txt', 'r', encoding='UTF-8')

for ts in range(1, 11):
    tg_len = int(input())

    str_table = []
    for _ in range(8):
        str_table.append(list(input()))

    p_cnt = 0
    for r in range(8):
        for c in range(8):
            if c + tg_len - 1 < 8:
                cnt_c = 0
                for i in range(tg_len//2):
                    if str_table[r][c+i] == str_table[r][c + tg_len - 1 - i]:
                        cnt_c += 1
                    if cnt_c == tg_len // 2:
                        p_cnt += 1
            if r + tg_len - 1 < 8:
                cnt_r = 0
                for i in range(tg_len//2):
                    if str_table[r+i][c] == str_table[r + tg_len - 1 - i][c]:
                        cnt_r += 1
                    if cnt_r == tg_len // 2:
                        p_cnt += 1

    print(f'#{ts} {p_cnt}')

sys.stdin.close()

