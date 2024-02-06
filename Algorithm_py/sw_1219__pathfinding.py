import sys

sys.stdin = open('./sw_1219__pathfinding__input.txt', 'r')


for _ in range(1, 11):
    path1 = [0]*100
    path2 = [0]*100

    ts, path_n = map(int, input().split())
    lst = list(map(int, input().split()))
    for i in range(0, path_n, 2):
        if path1[lst[i]]:
            path2[lst[i]] = lst[i+1]
        else:
            path1[lst[i]] = lst[i+1]

    stack = []
    i=0
    while 1:



sys.stdin.close()