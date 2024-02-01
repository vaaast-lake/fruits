import sys

sys.stdin = open('./sw_1954__snail-number__input.txt', 'r')

for ts in range(int(input())):
    N = int(input())

    result = [[0]*N for i in range(N)]
    result[0][0] = 1
    remote_ctr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cur_pos = [0, 0]
    num = 2
    while num < N**2 + 1:
        for i in range(4):
            #. cur_x, cur_y = cur_pos
            #. 위 코드로 next_x을 만들어, 혹은 cur_x + move_x 등으로 while 조건문을 확인하면
            #. while 안에서 cur_pos를 초기화 해도
            #. cur_x 가 초기화되지 않아 next_x 혹은 cur_x + move_x의 값 또한 초기화되지 않는다.
            #. 때문에 cur_pos의 값을 직접 인덱스로 접근해, 가장 최근 값을 확인해야 한다.
            move_x, move_y = remote_ctr[i]
            while -1 < cur_pos[0] + move_x < N and -1 < cur_pos[1] + move_y < N and not result[cur_pos[0] + move_x][cur_pos[1] + move_y]:
                result[cur_pos[0] + move_x][cur_pos[1] + move_y] = num
                cur_pos[0], cur_pos[1] = cur_pos[0] + move_x, cur_pos[1] + move_y
                num += 1

    print(f'#{ts+1}')
    for i in range(N):
        print(*result[i])



sys.stdin.close()