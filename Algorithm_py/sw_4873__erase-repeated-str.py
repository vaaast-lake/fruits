import sys

sys.stdin = open('./sw_4873__erase-repeated-str__input.txt', 'r')

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

    def peek(self):
        if self.isEmpty():
            Exception('Stack is empty')
        else:
            return self.s[self.top]

    def __str__(self):
        return str(self.s)

for ts in range(1, int(input())+1):
    string = input()
    str_len = len(string)

    stack = Stack(str_len)
    cnt = 1
    idx = 0
    stack.push(string[0])
    for i in range(1, str_len):
        if string[i] != stack.peek():
            stack.push(string[i])
        elif string[i] == stack.peek():
            stack.pop()


    print(f'#{ts} {stack.top+1}')

sys.stdin.close()