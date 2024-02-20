import sys
# from collections import deque

# sys.stdin = open('./bj_g4-3190__snake__input.txt', 'r')

input = sys.stdin.readline

#. Circular queue implementatino
class Queue:
    def __init__(self, size):
        self.size = size
        self.q = [None] * size
        self.front = self.rear = 0

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return
        self.front = (self.front + 1) % self.size
        return self.q[self.front]

    def enqueue(self, val):
        if self.is_full():
            print('queue is full')
            return
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = val

    def is_full(self):
        return self.front == (self.rear +1) % self.size

    def is_empty(self):
        return self.front == self.rear

    #. for check last factor in q
    def peek(self):
        return self.q[self.rear]


RIGHT = 'D'
LEFT = 'L'
APPLE = 2
WALL = -1
BODY = 1
EMPTY = 0


def init_table(apples_pos):
    table = [[-1] * (N+2)]
    table += [[-1] + [0] * N + [-1] for _ in range(N)]
    table += [[-1] * (N+2)]
    for pos in apples_pos:
        table[pos[0]][pos[1]] = APPLE

    return table


def dummy_move(direction):
    # cur_x, cur_y = d[0]
    cur_x, cur_y = q.peek()                                             #. 현재 머리 위치 확인
    move_x, move_y = remote_ctr[direction][0], remote_ctr[direction][1]
    next_x, next_y = cur_x + move_x, cur_y + move_y

    if table[next_x][next_y] == WALL or table[next_x][next_y] == BODY: #. 다음 위치가 벽 혹은 몸이라면 이동 실패
        return False
    else:
        # table[cur_x][cur_y] = BODY                                   #. 현재 머리 위치 기록 하거나
                                                                       #. 아래에서 다음 머리 위치를 표시해주기.
        if table[next_x][next_y] != APPLE:                             #. 사과가 아니라면 마지막 위치를 꼬리로 빼고
                                                                       #. 해당 위치를 빈 자리로 초기화
            # tail_x, tail_y = d.pop()
            tail_x, tail_y = q.dequeue()
            table[tail_x][tail_y] = EMPTY
        # d.appendleft((next_x, next_y))
        q.enqueue((next_x, next_y))                                  #. 다음 위치를 머리로 넣고 지도에 표시.
        table[next_x][next_y] = BODY                                 #. 다음 머리 위치 표시.

    return True


def start_dummy_game():
    direction = 0
    time = 0
    for t, vec in vector_info:              #. 리턴으로 중첩 반복문 탈출
        while time < t:                     #. 첫 번째 시간에 도달할 때까지 이동
            if not dummy_move(direction):   #. 이동 실패면 시간 하나 더하고 리턴. 아니면 시간 더한 후 반복
                time += 1
                return time
            time += 1
        if vec == RIGHT:                    #. 시간에 도달했다면 방향 전환
            direction = (direction + 1) % 4
        elif vec == LEFT:
            direction = (direction - 1) % 4
    else:                                   #. 방향 전환 이후에도 이동할 수 있다면 끝날 때까지 이동.
        while 1:
            if not dummy_move(direction):
                time += 1
                return time
            time += 1


N = int(input())
#. 사과 위치 정보
K = int(input())
apples_pos = [list(map(int, input().split())) for _ in range(K)]

#. 방향 전환 정보
L = int(input())
vector_info = [list(input().split()) for _ in range(L)]
#. 초 정보 int로 변환
for el in vector_info:
    el[0] = int(el[0])

table = init_table(apples_pos)
# d = deque()
# d.append((1, 1))
q = Queue(N**2)
q.enqueue((1, 1))


#. 오른쪽 방향 진행을 시작으로 시계방향으로 돌아가도록 controler를 구성.
remote_ctr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

print(start_dummy_game())


sys.stdin.close()