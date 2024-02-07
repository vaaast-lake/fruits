import sys

sys.stdin = open('./sw_1989__newbie-palindrome__input.txt', 'r')


for ts in range(1, int(input())+1):
    result = 0
    string = input()
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            break
    else:
        result = 1

    print(f'#{ts} {result}')


sys.stdin.close()