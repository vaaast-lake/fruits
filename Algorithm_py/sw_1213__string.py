import re
import sys

sys.stdin = open('./sw_1213__string__input.txt', 'r', encoding='UTF-8')

for ts in range(10):
    case_num = int(input())
    target = input()
    tg_len = len(target)
    string = input()
    st_len = len(string)

    # regEx = re.compile((target))
    # lst = regEx.findall(string)
    # print(f'#{ts+1} {len(lst)}')

    cnt = 0
    for i in range(st_len):
        for j in range(tg_len):
            if i + j < st_len and string[i+j] != target[j]:
                break
            if i + j < st_len and string[i+j] == target[j] and j == tg_len - 1:
                cnt += 1

    print(f'#{ts+1} {cnt}')

sys.stdin.close()