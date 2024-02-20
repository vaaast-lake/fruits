import sys
from collections import deque

# sys.stdin = open('./bj_g4-3190__snake__input.txt', 'r')

input = sys.stdin.readline

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
    cur_x, cur_y = d[0]
    move_x, move_y = remote_ctr[direction][0], remote_ctr[direction][1]
    next_x, next_y = cur_x + move_x, cur_y + move_y

    if table[next_x][next_y] == WALL or table[next_x][next_y] == BODY:
        return False
    else:
        table[cur_x][cur_y] = BODY
        if table[next_x][next_y] != APPLE:
            tail_x, tail_y = d.pop()
            table[tail_x][tail_y] = EMPTY
        d.appendleft((next_x, next_y))
        table[next_x][next_y] = BODY

    return True


def start_dummy_game():
    direction = 0
    time = 0
    for t, vec in vector_info:
        while time < t:
            if not dummy_move(direction):
                time += 1
                return time
            time += 1
        if vec == RIGHT:
            direction = (direction + 1) % 4
        elif vec == LEFT:
            direction = (direction - 1) % 4
    else:
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
d = deque()
d.append((1, 1))

#. 오른쪽 방향 진행을 시작으로 시계방향으로 돌아가도록 controler를 구성.
remote_ctr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

print(start_dummy_game())


sys.stdin.close()