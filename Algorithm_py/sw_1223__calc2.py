import sys

sys.stdin = open('sw_1223__calc2__input.txt', 'r')


priority = {'*': 2, '+': 1}

for ts in range(1, 11):

    string_len = int(input())
    string = input()

    postfix_stack = []
    postfix_str = ''
    for el in string:
        if el in '*+':
            if postfix_stack and \
                    priority[postfix_stack[-1]] >= priority[el]:
                while postfix_stack and \
                        priority[postfix_stack[-1]] >= priority[el]:
                    postfix_str += postfix_stack.pop()
            postfix_stack.append(el)
        else:
            postfix_str += el
    else:
        while postfix_stack:
            postfix_str += postfix_stack.pop()

    calc_stack = []
    for el in postfix_str:
        if el == '*':
            calc_stack.append(calc_stack.pop() * calc_stack.pop())
        elif el == '+':
            calc_stack.append(calc_stack.pop() + calc_stack.pop())
        else:
            calc_stack.append(int(el))

    print(f'#{ts} {calc_stack[-1]}')



sys.stdin.close()