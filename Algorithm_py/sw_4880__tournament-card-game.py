import sys

sys.stdin = open('./sw_4880__tournament-card-game__input.txt', 'r')

# 1 < 2, 2 < 3, 3 < 1


def compare(i, j, lst):
    win_idx = 0
    if lst[i] == lst[j]:
        if i > j:
            win_idx = j
        else:
            win_idx = i
    elif (lst[i] != 3 and lst[j] != 3) and \
            lst[i] != lst[j]:
        if lst[i] < lst[j]:
            win_idx = j
        else:
            win_idx = i
    elif lst[i] == 3 or lst[j] == 3:
        if lst[i] == 1 or lst[j] == 1:
            if lst[i] > lst[j]:
                win_idx = j
            else:
                win_idx = i
        elif lst[i] == 2 or lst[j] == 2:
            if lst[i] < lst[j]:
                win_idx = j
            else:
                win_idx = i

    return win_idx


def conq(l, m, r, lst):
    global last_win
    i = l
    j = m+1

    while i <= m and j <= r:
        if memo[i] and memo[j]:
            i += 1
            j += 1
            continue

        if memo[i]:
            i += 1
            continue
        elif memo[j]:
            j += 1
            continue

        last_win = compare(i, j, lst)

        memo[i], memo[j] = 1, 1
        memo[last_win] = 0
        i += 1
        j += 1

    while i <= m:
        if memo[i]:
            i += 1
            continue
        memo[last_win], memo[i] = 1, 1
        last_win = compare(last_win, i, lst)
        memo[last_win] = 0
        i += 1

    while j <= r:
        if memo[j]:
            j += 1
            continue
        memo[last_win], memo[j] = 1, 1
        last_win = compare(last_win, j, lst)
        memo[last_win] = 0
        j += 1



def div(l, r, lst):
    if l >= r:
        return

    m = (l + r) // 2
    div(l, m, lst)
    div(m+1, r, lst)
    conq(l, m, r, lst)


for tc in range(1, int(input())+1):
    N = int(input())

    cards = list(map(int, input().split()))
    memo = [0]*N
    last_win = 0

    div(0, N-1, cards)

    print(f'#{tc} {last_win+1}')

sys.stdin.close()

