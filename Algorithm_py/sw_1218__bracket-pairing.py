import sys

sys.stdin = open('./sw_1218__bracket-pairing__input.txt', 'r')

for ts in range(1, 11):
    lst_len = int(input())
    lst = list(input())

    stack = []
    valid = 1
    for i in range(lst_len):
        if lst[i] == '{' or lst[i] == '[' or lst[i] == '(' or lst[i] == '<':
            stack.append(lst[i])
        else:
            if lst[i] == ')' and stack.pop() == '(':
                continue
            if lst[i] == '}' and stack.pop() == '{':
                continue
            if lst[i] == '>' and stack.pop() == '<':
                continue
            if lst[i] == ']' and stack.pop() == '[':
                continue
            else:
                valid = 0
                break

    print(f'#{ts} {valid}')

sys.stdin.close()