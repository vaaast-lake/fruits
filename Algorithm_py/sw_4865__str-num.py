import sys

sys.stdin = open('./sw_4865__str-num__input.txt', 'r')

for ts in range(1, int(input())+1):
    s1, s2 = input(), input()

    dic = {}
    for el in s1:
        dic[el] = 0

    for el in s2:
        if el in dic:
            dic[el] += 1

    max_v = 0
    for el in dic.values():
        if max_v < el:
            max_v = el

    print(f'#{ts} {max_v}')

sys.stdin.close()