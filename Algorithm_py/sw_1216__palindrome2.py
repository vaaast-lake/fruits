import sys

sys.stdin = open('./sw_1216__palindrome2__input.txt', 'r', encoding='UTF-8')

#. str_table을 함수 스코프 안에 넣어주면 더 느려짐


def find_max_p_len(p_len, lst):
    for i in range(0, 100):
        for j in range(0, 100 - p_len+1):
            if lst[i][j] == lst[i][j + p_len - 1]:
                #. 0번째 확인해줬으니, 1번부터 시작하면 되고,
                #. 이 부분을 무시하면 매 행/열 마다 한 번씩 더 확인해
                #. 시간이 조금 더 걸린다 (25ms)
                for k in range(1, p_len // 2):
                    if lst[i][j+k] != lst[i][j + p_len-1 - k]:
                        break
                else:
                    return True

            if lst[j][i] == lst[j + p_len-1][i]:
                for k in range(1, p_len//2):
                    if lst[j + k][i] != lst[j + p_len-1 - k][i]:
                        break
                else:
                    return True
    return False


for _ in range(0, 10):
    tc = int(input())

    str_table = [list(input()) for _ in range(100)]

    for p_len in range(100, 0, -1):
        if find_max_p_len(p_len, str_table):
            print(f'#{tc} {p_len}')
            break

sys.stdin.close()