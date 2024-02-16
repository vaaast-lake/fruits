import sys

sys.stdin = open('./sw_1225__password-creater__input.txt', 'r')


class Queue:                                       #. 큐 구현
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.s = [0] * self.size

    def enqueue(self, v):
        if self.is_full():
            print('queue is full')
            return
        self.rear = (self.rear+1) % self.size
        self.s[self.rear] = v

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return
        self.front = (self.front+1) % self.size
        return self.s[self.front]

    def is_full(self):
        return self.front == (self.rear+1) % self.size

    def is_empty(self):
        return self.front == self.rear

    #. def print(self):                        #. 큐 요소 반환
    #.     tmp = [0] * (self.size-1)           #. 요소가 들어갈 임시 배열 생성
    #.     j = 0                               #. 임시 배열의 인덱스
    #.     i = (self.front+1) % self.size      #. 큐를 돌기 위한 인덱스
    #.     while j < self.size-1:              #. 임시 배열은 큐 사이즈보다 하나 더 작아야 함
    #.         tmp[j] = self.s[i]
    #.         i = (i + 1) % self.size
    #.         j += 1
    #.
    #.     return tmp

    def peek_right(self):                   #. 큐 가장 오른쪽 요소 확인
        return self.s[self.rear]


#. def create_password():                   #. while loop (중첩 반복문) 사전 종료를 위해 함수 구현
#.     while 1:
#.         for i in range(1, 6):
#.             val = q.dequeue()
#.             val = val - i if val >= i else 0
#.             q.enqueue(val)
#.             if not q.peek_right():
#.                 return


for _ in range(1, 11):
    tc = int(input())
    nums = list(map(int, input().split()))

    q = Queue(len(nums)+1)
    for el in nums:
        q.enqueue(el)

    #. create_password()

    flag = True
    while flag:                              #. 플래그로 while loop 탈출
        for i in range(1, 6):
            val = q.dequeue()
            val = val - i if val >= i else 0
            q.enqueue(val)
            if not q.peek_right():
                flag = False
                break

    print(f'#{tc}', *[q.dequeue() for _ in range(q.size-1)])


sys.stdin.close()