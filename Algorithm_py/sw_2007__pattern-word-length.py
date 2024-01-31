import sys

sys.stdin = open('./sw_2007__pattern-word-length__input.txt', 'r')

for ts in range(int(input())):
    string = input()
    str_len = len(string)
    for i in range(1, 10):
        if string[:i] == string[i:i+i]:
            print(f'#{ts+1} {i}')
            break


sys.stdin.close()