import sys

sys.stdin = open('./sw_3143__fastest-string-typing__input.txt', 'r')


def check_pattern(s1, s2, idx):
    for i in range(1, len(s2)):
        if s2[s2_len-1 - i] != s1[idx + s2_len-1 - i]:
            break
    else:
        return True

    return False


for ts in range(1, int(input())+1):
    s1, s2 = input().split()
    s1_len = len(s1)
    s2_len = len(s2)

    i = 0
    cnt = 0
    while i < s1_len:
        if i + s2_len-1 < s1_len and s1[i + s2_len-1] == s2[s2_len-1] and check_pattern(s1, s2, i):
            i += s2_len
            cnt += 1
        else:
            i += 1
            cnt += 1

    print(f'#{ts} {cnt}')



sys.stdin.close()