import sys
from collections import deque

sys.stdin = open('./sw_1242__scan-password__input.txt', 'r')

input = sys.stdin.readline
print = sys.stdout.write

valid_back_code = {
    '1': True,
    '3': True,
    '5': True,
    '7': True,
    '9': True,
    'B': True,
    'D': True,
    'F': True
}

valid_code = {
    (3, 2, 1, 1): '0',
    (2, 2, 2, 1): '1',
    (2, 1, 2, 2): '2',
    (1, 4, 1, 1): '3',
    (1, 1, 3, 2): '4',
    (1, 2, 3, 1): '5',
    (1, 1, 1, 4): '6',
    (1, 3, 1, 2): '7',
    (1, 2, 1, 3): '8',
    (3, 1, 1, 2): '9',
}


def check_last_code(r, c):
    if not valid_back_code.setdefault(table[r][c], None):
        return False
    return True


def print_code(r, c):
    tmp_deque = deque()
    while c > -1 and table[r][c]:
        tmp_deque.appendleft(table[r][c])
        c -= 1
    return ''.join(tmp_deque)


def get_inst_code(idx):
    cnt = 4
    cnt3 = cnt2 = cnt1 = cnt0 = 0
    prev = cur = binary[idx]
    last_check_idx = 0
    for i in range(idx, -1, -1):
        cur = binary[i]
        if prev != cur:
            cnt -= 1

        if cnt == 4:
            cnt3 += 1
        elif cnt == 3:
            cnt2 += 1
        elif cnt == 2:
            cnt1 += 1
        elif cnt == 1:
            cnt0 += 1
        else:
            last_check_idx = i
            break

        prev = cur

    tmp_code = [cnt0, cnt1, cnt2, cnt3]
    gcd = tmp_code[0]
    for i in range(1, 4):
        gcd = get_gcd(gcd, tmp_code[i])

    return (last_check_idx, (cnt0 // gcd, cnt1 // gcd, cnt2 // gcd, cnt3 // gcd))


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for tc in range(int(input())):
    N, M = map(int, input().split())

    table = [list(input()) for _ in range(N)]

    valid_r = 0
    valid_c = 0
    for r in range(N-1, -1, -1):
        for c in range(M-1, -1, -1):
            if check_last_code(r, c):
                valid_r = r
                valid_c = c
                break

    code = print_code(valid_r, valid_c)

    code_len = len(code)
    binary = bin(int(code, 16)).replace('0b', '')
    bi_len = len(binary)

    result = 0
    for i in range(bi_len-1, -1, -1):
        idx = i
        cnt = 8
        nums = [0] * 8
        nums_idx = 7
        while cnt:
            if binary[idx] != '0':
                check_code = get_inst_code(idx)
                last_idx = check_code[0]
                inst_code = check_code[1]
                # print(f'inst_code: {inst_code}\n')
                #. 뒤에서부터 코드 확인, 맞으면 계속. 아니면 한 칸 이동 후 계속.
                if valid_code.setdefault(inst_code, None):
                    # print(f'inst_code: {inst_code}\ncnt: {cnt}\n')
                    nums[nums_idx] = valid_code[inst_code]
                    idx = last_idx
                    nums_idx -= 1
                    cnt -= 1
                else:
                    break
            else:
                break
        if not cnt:
            odd = even = 0
            for i in range(8):
                if not i % 2:
                    even += nums[i]
                else:
                    odd += nums[i]
            # print(f'#{tc} {odd}, {even}\n')
            result = odd * 3 + even if not odd * 3 + even % 10 else 0

    # print(f'#{tc} {result}\n')


    print(f'#{tc}: ')
    print(f'code: {code}, ')
    print(f'binary: {binary}\n')





sys.stdin.close()