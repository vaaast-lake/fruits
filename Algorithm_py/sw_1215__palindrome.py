import sys

sys.stdin = open('./sw_1215__palindrome__input.txt', 'r', encoding='UTF-8')

for _ in range(10):
    tg_len = int(input())

    str_table = []
    for _ in range(8):
        str_table.append(list(input()))

    p_cnt = 0
    for r in range(8):
        for c in range(8):
            if c + tg_len - 1 < 8:
                for i in range(tg_len//2-1):
                    cnt = 0
                    if str_table[r][c+i] == str_table[r][c + tg_len - 1 - i]:
                        cnt += 1
                    if cnt == tg_len:
                        p_cnt += 1
    print(p_cnt)

sys.stdin.close()

