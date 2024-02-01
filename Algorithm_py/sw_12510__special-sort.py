import sys

sys.stdin = open('./sw_12510__special-sort__input.txt', 'r')

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


for ts in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    nums_len = len(nums)
    sorted_nums = merge_sort(nums)

    result = []
    for i in range(nums_len-1, -1, -1):
        result.append(sorted_nums[i])
        result.append(sorted_nums[nums_len - 1 - i])
        if len(result) == 10:
            break

    print(f"#{ts+1} {' '.join(map(str,result))}")

sys.stdin.close()



