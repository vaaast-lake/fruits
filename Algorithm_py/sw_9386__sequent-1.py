import sys

sys.stdin = open('./sw_9386__sequent-1__input.txt', 'r', encoding='UTF-8')

for ts in range(1, int(input()) + 1):
    num_seq_len = int(input())
    seq = int(input())

    max_len = 0
    cnt = 1 if seq % 10 else 0
    while seq:
        seq //= 10
        if seq % 10:
            cnt += 1
        else:
            if max_len < cnt:
                max_len = cnt
            cnt = 0

    print(f'#{ts} {max_len}')

sys.stdin.close()