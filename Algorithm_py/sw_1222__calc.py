import sys

sys.stdin = open('sw_1222__calc__input.txt', 'r')


for ts in range(1, 11):
    string_len = int(input())
    string = input()

    stack = []
    for i in range(string_len):
        if string[i] != '+':
            if stack and stack[-1] == '+':
                tmp = stack.pop()
                stack.append(string[i])
                stack.append(tmp)
            else:
                stack.append(string[i])
        else:
            stack.append(string[i])

    stack2 = []
    for el in stack:
        if el == '+':
            stack2.append(int(stack2.pop()) + int(stack2.pop()))
        else:
            stack2.append(el)

    print(f'#{ts} {stack2[-1]}')



sys.stdin.close()