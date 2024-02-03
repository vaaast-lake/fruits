def can_result(maxLength, ls):
    for i in range(0, 100):
        # 가로 회문
        for j in range(0, 100 - maxLength + 1):
            if (ls[i][j] == ls[i][j + maxLength - 1]):
                for k in range(maxLength // 2):
                    if (ls[i][j + k] != ls[i][j + maxLength - k - 1]):
                        break
                else:
                    return True

        # 세로
        for j in range(0, 100 - maxLength + 1):
            if ls[j][i] == ls[j + maxLength - 1][i]:
                for k in range(1, maxLength // 2):
                    if ls[j + k][i] != ls[j + maxLength - 1 - k][i]:
                        break
                else:
                    return True


for i in range(0, 10):
    caseNumber = int(input())
    ls = [list(input()) for i in range(100)]
    for maxLength in range(100, -1, -1):
        if can_result(maxLength, ls):
            print(f"#{caseNumber} {maxLength}")
            break