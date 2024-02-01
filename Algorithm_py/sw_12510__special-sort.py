import sys

sys.stdin = open('./sw_12510__special-sort__input.txt', 'r')

def selectionSort(lst, lst_len):
    for i in range(lst_len-1):
        minIdx = i
        for j in range(i+1, lst_len):
            if lst[minIdx] > lst[j]:
                minIdx = j
        lst[i], lst[minIdx] = lst[minIdx], lst[i]

for ts in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    nums_len = len(nums)
    selectionSort(nums, nums_len)

    result = []
    for i in range(nums_len-1, -1, -1):
        result.append(nums[i])
        result.append(nums[nums_len - 1 - i])
        if len(result) == 10:
            break

    print(f"#{ts+1} {' '.join(map(str,result))}")

sys.stdin.close()



