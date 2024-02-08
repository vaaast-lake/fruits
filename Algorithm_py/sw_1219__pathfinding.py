import sys

sys.stdin = open('./sw_1219__pathfinding__input.txt', 'r')


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = 0
        self.rear = 0

    def enqueue(self, val):
        if self.is_full():
            print('queue full')
            return
        self.rear = (self.rear+1) % self.size
        self.queue[self.rear] = val

    def dequeue(self):
        if self.is_empty():
            print('queue empty')
            return
        self.front = (self.front+1) % self.size
        return self.queue[self.front]

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def is_full(self):
        if self.front == (self.rear+1) % self.size:
            return True
        else:
            return False


def bfs(edges, visit, node):
    if node == 99:
        return 1

    visit[node] = True
    for adj_nd in edges[node]:
        if not visit[adj_nd]:
            queue.enqueue(adj_nd)

    if not queue.is_empty():
        next_node = queue.dequeue()
        return bfs(edges, visit, next_node)
    else:
        return 0


for _ in range(1, 11):
    tc, edge_n = map(int, input().split())

    edges = [[] for _ in range(100)]
    visit = [False for _ in range(100)]
    queue = CircularQueue(edge_n)

    data = list(map(int, input().split()))
    for i in range(0, edge_n*2, 2):
        edges[data[i]].append(data[i+1])

    result = bfs(edges, visit, 0)
    print(f'#{tc} {result}')


sys.stdin.close()