import sys

sys.stdin = open('./sw_5097__rotation__input.txt', 'r')


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


for tc in range(1, int(input())+1):
    N, M = list(map(int, input().split()))

    lst = list(map(int, input().split()))
    # lst_len = len(lst)


    # q = Queue(N+1)

    # for i in range(N):
    #     q.enqueue(lst[i])
    #
    # for _ in range(M):
    #     tmp = q.dequeue()
    #     q.enqueue(tmp)

    # print(f'#{tc} {q.dequeue()}')
    # print(f'#{tc} {lst[M%len(lst)]}')
    print(f'#{tc} {lst[M%N]}')



# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




sys.stdin.close()