import sys

sys.stdin = open('sw_4874__forth__input.txt', 'r')


for tc in range(1, int(input())+1):

    expr = input().split()

    result = 0
    stack = []
    for i in range(len(expr)):
        if expr[i] in '*+/-':
            if len(stack) < 2:
                result = 'error'
                break
            elif expr[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif expr[i] == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif expr[i] == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 // num1)
            elif expr[i] == '+':
                stack.append(stack.pop() + stack.pop())
        elif expr[i] == '.':
            # if i != len(expr) - 1:
            #     result = 'error'
            break
        elif expr[i].isdecimal():
            stack.append(int(expr[i]))
        else:
            result = 'error'
            break

    if result == 'error' or len(stack) != 1: #. len(expr) < 3
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack[0]}')

sys.stdin.close()