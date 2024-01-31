import sys

sys.stdin = open('./sw_12470__number-card__input.txt', 'r')


for tc in range(int(input())):
    card_num = int(input())
    cards = input()

    num_list = [0]*10
    for i in range(len(cards)):
        num_list[int(cards[i])] += 1

    max_n = 0
    max_c = 0
    for i in range(len(num_list)):
        if max_c <= num_list[i]:
            max_n = i
            max_c = num_list[i]

    print(f'#{tc+1} {max_n} {max_c}')


f.close()