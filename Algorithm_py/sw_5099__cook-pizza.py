import sys

sys.stdin = open('./sw_5099__cook-pizza__input.txt', 'r')


#. queue 구현
class Queue:
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


for tc in range(1, int(input())+1):
    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    #. 큐 요소와 인덱스를 하나의 배열에 묶어줌
    #. 피자에 테그 붙여주기, 라벨 붙여주기
    labeling = [[i+1, val] for i, val in enumerate(lst)]
    q = Queue(N+1)

    #. 화덕(queue) 갯수만큼 넣음
    for i in range(N):
        q.enqueue(labeling[i])

    cnt = 0
    next_pizz = N
    #. 하나의 피자가 남을 때까지 반복
    while cnt < M-1:
        #. 피자 꺼내서 확인
        i, cheese = q.dequeue()
        cheese //= 2
        #. 다 녹았다면
        if cheese == 0:
            #. 녹은 피자 수 카운트
            cnt += 1
            #. 다음 피자가 있다면
            if next_pizz < M:
                #. 넣어주고
                q.enqueue(labeling[next_pizz])
                #. 다음다음 피자 준비
                next_pizz += 1
        else:
            #. 다 안 녹았으면 다시 넣어줌
            q.enqueue([i, cheese])
    #. 마지막 남은 피자 꺼내서
    last_one = q.dequeue()
    #. 라벨만 출력
    result = last_one[0]

    print(f'#{tc} {result}')


sys.stdin.close()


