import sys

sys.stdin = open('./sw_4886__check-bracket__input.txt', 'r')

class Stack:
    def __init__(self, size):
        self.size = size
        self.s = [None] * size
        self.top = -1

    def push(self, value):
        if self.isFull():
            Exception("Stack is full")
        else:
            self.top += 1
            self.s[self.top] = value

    def pop(self):
        if self.isEmpty():
            Exception("stack is empty")
        else:
            result = self.s[self.top]
            self.s[self.top] = None
            self.top -= 1
            return result

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top > self.size-1:
            return True
        else:
            return False

for ts in range(1, int(input())+1):
    string = input()
    str_len = len(string)

    st_size = 0
    for i in range(str_len):
        if string[i] == '{' or string[i] == '(' or \
                string[i] == ')' or string[i] == '}':
            st_size += 1

    st = Stack(st_size)
    result = 1
    for i in range(str_len):
        if string[i] == '{' or string[i] == '(':
            st.push(string[i])
        elif string[i] == '}' and st.pop() != '{':
            result = 0
            break
        elif string[i] == ')' and st.pop() != '(':
            result = 0
            break

    if not st.isEmpty():
        result = 0

    print(f'#{ts} {result}')

sys.stdin.close()