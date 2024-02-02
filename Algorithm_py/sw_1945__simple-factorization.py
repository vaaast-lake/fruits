import sys

sys.stdin = open('./sw_1945__simple-factorization___input.txt', 'r', encoding='UTF-8')

for ts in range(int(input())):

    num = int(input())
    nums = [0] * 12
    div_nums = [2, 3, 5, 7, 11]

    for div_num in div_nums:
        while 1:
            if not num % div_num:
                nums[div_num] += 1
                num //= div_num
            else:
                break

    print(f'#{ts+1}', end=' ')
    for div_num in div_nums:
        print(f'{nums[div_num]}', end=' ')
    print()


sys.stdin.close()