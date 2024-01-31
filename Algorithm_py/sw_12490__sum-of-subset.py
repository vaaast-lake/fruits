import sys

sys.stdin = open('./sw_12490__sum-of-subset__input.txt', 'r')

lst = [i for i in range(1, 13)]
lst_len = len(lst)

for ts in range(int(input())):
    N, K = map(int, input().split())

    result = []
    for i in range(1 << lst_len):
        tmp = []
        for j in range(lst_len):
            if i & (1 << j):
                tmp.append(lst[j])
        result.append(tmp)

    cnt = 0
    for el in result:
        if len(el) == N:
            result_sum = 0
            for j in el:
                result_sum += j
            if result_sum == K:
                cnt += 1
    print(f'#{ts + 1} {cnt}')


sys.stdin.close()