import sys

sys.stdin = open('./sw_1219__pathfinding__input.txt', 'r')


# class CircularQueue:
#     def __init__(self, size):
#         self.size = size
#         self.queue = [None]*size
#         self.front = 0
#         self.rear = 0
#
#     def enqueue(self, val):
#         if self.is_full():
#             print('queue full')
#             return
#         self.rear = (self.rear+1) % self.size
#         self.queue[self.rear] = val
#
#     def dequeue(self):
#         if self.is_empty():
#             print('queue empty')
#             return
#         self.front = (self.front+1) % self.size
#         return self.queue[self.front]
#
#     def is_empty(self):
#         if self.front == self.rear:
#             return True
#         else:
#             return False
#
#     def is_full(self):
#         if self.front == (self.rear+1) % self.size:
#             return True
#         else:
#             return False
#
#
# def bfs(edges, visit, node):
#     if node == 99:
#         return 1
#
#     visit[node] = True
#     for adj_nd in edges[node]:
#         if not visit[adj_nd]:
#             queue.enqueue(adj_nd)
#
#     if not queue.is_empty():
#         next_node = queue.dequeue()
#         return bfs(edges, visit, next_node)
#     else:
#         return 0

class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.s = [None]*self.size

    def push(self, val):
        if self.is_full():
            print('stack is full')
            return
        self.top += 1
        self.s[self.top] = val

    def pop(self):
        if self.is_empty():
            print('stack is empty')
            return
        val = self.s[self.top]
        self.top -= 1
        return val

    def peek(self):
        if self.is_empty():
            print('stack is empty')
        else:
            return self.s[self.top]

    def is_full(self):
        if self.top > self.size-1:
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False


# def dfs(edges, visit, node):
#     if node == 99:
#         return 1
#
#     visit[node] = True
#     for i in range(len(edges[node])):
#         next_nd = edges[node][i]
#         if not visit[next_nd]:
#             if dfs(edges, visit, next_nd):
#                 return 1
#     return 0

def iter_dfs(edges, start, st_size):
    stack = Stack(st_size)
    stack.push(start)

    visit = [False for _ in range(100)]
    visit[start] = True
    while not stack.is_empty():
        cur = stack.peek()
        for next_nd in edges[cur]:
            if next_nd == 99:
                return 1
            if not visit[next_nd]:
                visit[next_nd] = True
                stack.push(next_nd)
                break
        else:
            stack.pop()
    return 0



for _ in range(1, 11):
    tc, edge_n = map(int, input().split())

    edges = [[] for _ in range(100)]
    # visit = [False for _ in range(100)]
    # queue = CircularQueue(edge_n)
    # stack = Stack(edge_n)

    data = list(map(int, input().split()))
    for i in range(0, edge_n*2, 2):
        edges[data[i]].append(data[i+1])

    # result = bfs(edges, visit, 0)
    # result = dfs(edges, visit, 0)
    result = iter_dfs(edges, 0, edge_n)
    print(f'#{tc} {result}')


sys.stdin.close()