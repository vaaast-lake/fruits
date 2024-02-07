import sys

sys.stdin = open('./sw_2005__Pascal\'s-Triangle__input.txt', 'r')

for ts in range(1, int(input())+1):
    N = int(input())
    pasc = [0]*N
    memo = [0]*N
    pasc[0] = 1
    pasc_len = len(pasc)

    i = 0
    while pasc[pasc_len-1] == 0:
        if pasc[i+1] == 0:
            pasc[i+1] = 1
            i = 0
            continue
        else:
            memo[i] = pasc[i+1]
            pasc[i+1] = memo[i] + pasc[i]
            i += 1

    print(pasc)



sys.stdin.close()