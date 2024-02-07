import sys

sys.stdin = open('./sw_4864__compare-string__input.txt', 'r')

for ts in range(1, int(input()) + 1):
    target = input()
    string = input()

    target_len = len(target)
    string_len = len(string)

    result = 0
    for i in range(string_len - target_len + 1):
        if string[i] != target[0]:
            continue
        else:
            for j in range(1, target_len):
                if string[i+j] != target[j]:
                    break
            else:
                result = 1


    print(f'#{ts} {result}')





sys.stdin.close()