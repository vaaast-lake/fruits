import sys

sys.stdin = open('./sw_1227__maze2__input.txt', 'r')

# 값 입력 실수하는 거 방지용 Const
WALL = '1'
GOAL = '3'
SIZE = 100

# dfs는 터진다. 최악의 경우, 98칸의 길이 한 칸을 간격으로 49개가 있을 때,
# 콜 스택은 약 5000개가 쌓인다.
# 파이썬 스택은 기본값으로 1000이라 터져벌임
def bfs():
    remote_ctr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = [0] * (SIZE ** 2)

    # 차피 넣고 시작햐야하니 rear는 1로
    front = 0
    rear = 1
    q[rear] = (1, 1)
    visited[1][1] = 1

    while front != rear:                              # 큐가 비었다면 whlile loop 종료
        front = (front + 1) % SIZE
        cur_x, cur_y = q[front]

        if table[cur_x][cur_y] == GOAL:
            return 1

        for i in range(4):
            nx_x, nx_y = cur_x + remote_ctr[i][0], cur_y + remote_ctr[i][1]
            if table[nx_x][nx_y] != WALL and not visited[nx_x][nx_y] and \
                    visited[cur_x][cur_y] > visited[nx_x][nx_y]:             # 벽이 아니고,
                                                                             # 방문 순서가 더 적거나 없는 경우

                visited[nx_x][nx_y] = visited[cur_x][cur_y] + 1              # 이전 방문 순서에서 1을 더해줘
                                                                             # 현재 방문 순서를 기록
                rear = (rear + 1) % SIZE
                q[rear] = (nx_x, nx_y)
    return 0


for _ in range(1, 11):

    tc = int(input())
    table = [list(input()) for _ in range(SIZE)]
    visited = [[0]*SIZE for _ in range(SIZE)]
    result = bfs()

    print(f'#{tc} {result}')

sys.stdin.close()