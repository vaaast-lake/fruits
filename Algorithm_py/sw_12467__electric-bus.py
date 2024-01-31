import sys

#. K: 한 번 충전으로 이동할 수 있는 최대 정류장 수
#. M: 충전기가 설치된 정류장 수
#. N: 종점 정류장 번호

sys.stdin = open('./sw_12467__electric-bus__input.txt', 'r')

line_n = int(input())
for line in range(line_n):
    max_move, last_station, charge_stations = list(map(int, input().split()))
    charge_station = list(map(int, input().split()))
    charge_cnt = 0
    cur_pos = 0
    next_pos = 0

    for i in range(cur_pos, charge_stations):
        next_pos = cur_pos + max_move
        if next_pos > charge_station[i]:
            if i == charge_stations - 1:
                if charge_station[i] + max_move >= last_station:
                    charge_cnt += 1
                    cur_pos = charge_station[i] + max_move
                    break
                else:
                    cur_pos = charge_station[i] + max_move
                    charge_cnt = 0
                    break
            continue
        elif next_pos == charge_station[i]:
            charge_cnt += 1
            cur_pos = charge_station[i]
            break
        elif next_pos < charge_station[i]:
            if cur_pos == charge_station[i-1]:
                charge_cnt = 0
                break
            charge_cnt += 1
            cur_pos = charge_station[i-1]
            break

    print(f'#{line+1} {charge_cnt}')












    # while cur_pos < last_station:
    #     flag = False
    #     #. for ... else 쓰면 flag 없이 코드 짤 수 있음.
    #     for move_to_pos in range(cur_pos + max_move, cur_pos - 1, -1):
    #         if move_to_pos >= last_station:
    #             cur_pos = move_to_pos
    #             break
    #         if (move_to_pos in charge_station_n) and (move_to_pos != cur_pos):
    #             cur_pos = move_to_pos
    #             charge_cnt += 1
    #             break
    #         if move_to_pos == cur_pos:
    #             flag = True
    #     if flag:
    #         charge_cnt = 0
    #         cur_pos = last_station
    # print(f'#{i+1} {charge_cnt}')

sys.stdin.close()

