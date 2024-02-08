import sys

sys.stdin = open('./sw_4869__join-paper__input.txt', 'r')

#. 1, 3, 5, 11, 21, 43, 85

for ts in range(1, int(input())+1):
    N = int(input())

    dp = [0] * (N//10)
    dp[0], dp[1] = 1, 3

    for i in range(2, N//10):
        dp[i] = dp[i-2] *2 + dp[i-1]

    print(f'#{ts} {dp[-1]}')


sys.stdin.close()