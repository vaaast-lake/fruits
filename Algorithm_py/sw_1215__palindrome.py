import sys

sys.stdin = open('./sw_1215__palindrome__input.txt', 'r', encoding='UTF-8')

for _ in range(10):
    tg_len = int(input())

    str_table = []
    for _ in range(8):
        str_table.append(list(input()))

    for r in range(8):
        for c in range(8):
            if r + tg_len < 8:
                for i in range(tg_len//2-1):
                    cnt = 0
                    if str_table[r + i] == str_table[r + tg_len - 1 - i]:
                        

sys.stdin.close()