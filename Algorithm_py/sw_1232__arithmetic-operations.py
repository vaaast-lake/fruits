import sys

sys.stdin = open('./sw_1232__arithmetic-operations__input.txt', 'r')

DIV = '/'
MULTI = '*'
SUB = '-'
PLUS = '+'
LEFT_CHILD = 0
RIGHT_CHILD = 3
OPR = 1
VAL = 2


#. 5번 케이스 56은 106, 107을 자식으로 둔다.


def arith_opr(opr, num1, num2):
    num1, num2 = int(num1), int(num2)
    if opr == DIV:
        if num1 == 0 or num2 == 0:
            return str(0)
        return str(num1 // num2)
    if opr == MULTI:
        return str(num1 * num2)
    if opr == SUB:
        return str(num1 - num2)
    if opr == PLUS:
        return str(num1 + num2)


def post_order(root=1):
    left = opr_heap[root][LEFT_CHILD]
    right = opr_heap[root][RIGHT_CHILD]
    opr = opr_heap[root][OPR]
    if not opr_heap[root][VAL]:
        num1 = post_order(left)
        num2 = post_order(right)
        opr_heap[root][VAL] = arith_opr(opr, num1, num2)

    return opr_heap[root][VAL] if opr_heap[root][VAL] else 0


for tc in range(1, 11):
    N = int(input())

    data = [input().split() for _ in range(N)]
    # print(data)
    opr_heap = [[None] * 4 for _ in range(N+1)]
    for el in data:
        node = int(el[0])
        if len(el) == 4:
            opr_heap[node][LEFT_CHILD] = int(el[2])
            opr_heap[node][OPR] = el[1]
            opr_heap[node][RIGHT_CHILD] = int(el[3])
        else:
            opr_heap[node][VAL] = el[1]

    post_order()
    # print(opr_heap)
    print(f'#{tc} {opr_heap[1][VAL]}')

sys.stdin.close()