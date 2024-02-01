import sys

sys.stdin = open('./sw_12510__special-sort__input.txt', 'r')

for ts in range(int(input())):
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    nums_len = len(nums)

    result = []
    for i in range(nums_len-1, -1, -1):
        result.append(nums[i])
        result.append(nums[nums_len - 1 - i])
        if len(result) == 10:
            break

    print(f"#{ts+1} {' '.join(map(str,result))}")

sys.stdin.close()



