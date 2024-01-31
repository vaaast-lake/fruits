for t in range(10):
    dump_n = int(input())
    boxes_lst = sorted(list(map(int, input().split())))

    for _ in range(dump_n):
        boxes_lst[-1] -= 1
        boxes_lst[0] += 1
        boxes_lst.sort()

    print(f'#{t+1} {boxes_lst[-1] - boxes_lst[0]}')