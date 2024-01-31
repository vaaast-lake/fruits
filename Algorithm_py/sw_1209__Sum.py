
for _ in range(10):
    case_num = int(input())
    num_table = [0]*100

    row_sum = [0]*100
    col_sum = [0]*100
    rd_sum = 0
    ld_sum = 0
    for i in range(100):
        num_table[i] = list(map(int, input().split()))
        row_sum[i] = sum(num_table[i])
        rd_sum += num_table[i][i]
        ld_sum += num_table[i][99-i]
        for j in range(100):
            col_sum[j] += num_table[i][j]

    max_v = max(rd_sum, ld_sum, *row_sum, *col_sum)
    print(f'#{case_num} {max_v}')







    #     for j in range(100):
    #         row_sum[i] += num_table[i][j]
    #         col_sum[j] += num_table[i][j]
    #         if i == j:
    #             rd_sum += num_table[i][j]
    #         if i + j == 99:
    #             ld_sum += num_table[i][j]
    # for i in range(100):
    #     if max_sum < row_sum[i]:
    #         max_sum == row_sum[i]
    #     if max_sum < col_sum[i]:
    #         max_sum == col_sum[i]
    # if max_sum < rd_sum:
    #     max_sum = rd_sum
    # if max_sum < ld_sum:
    #     max_sum = ld_sum

    # print(f'#{case_num} {max_sum}')