import sys

sys.stdin = open('./sw_5099__cook-pizza__input.txt', 'r')

# class Queue:
#     def __init__(self, size):
#         self.size = size
#         self.front = 0
#         self.rear = 0
#         self.s = [0] * self.size
#
#     def enqueue(self, v):
#         if self.is_full():
#             print('queue is full')
#             return
#         self.rear = (self.rear+1) % self.size
#         self.s[self.rear] = v
#
#     def dequeue(self):
#         if self.is_empty():
#             print('queue is empty')
#             return
#         self.front = (self.front+1) % self.size
#         return self.s[self.front]
#
#     def is_full(self):
#         return self.front == (self.rear+1) % self.size
#
#     def is_empty(self):
#         return self.front == self.rear


def find_last_p(N, M):
    cnt = 0
    result = 0

    while 1:
        for i in range(N):
            if lst[i] == 0:
                continue
            lst[i] = lst[i] // 2
            if lst[i] == 0:
                if N + 1 < M:
                    N += 1
                cnt += 1
            if cnt == done:
                result = i + 1
                return result
            else:
                break

for tc in range(1, int(input())+1):
    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    done = M-1
    cnt = 0
    result = find_last_p(N, M)

    print(f'#{tc} {result}')





sys.stdin.close()


