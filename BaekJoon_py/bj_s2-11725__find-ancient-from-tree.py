import sys

sys.stdin = open('./bj_s2-11725__find-ancient-from-tree__input.txt', 'r')

class Queue:
    def __init__(self, size):
        self.size = size
        self.q = [None] * self.size
        self.front = self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, val):
        if self.is_full():
            print('queue is full')
            return False
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = val

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return False
        self.front = (self.front + 1) % self.size
        return self.q[self.front]


def init_tree(root=1):
    q.enqueue(root)

    while not q.is_empty():
        root = q.dequeue()
        for i in range(len(adj[root])):
            if not visited[adj[root][i]]:
                q.enqueue(adj[root][i])
                visited[adj[root][i]] = True
                parent[adj[root][i]] = root


N = int(input())
parent = [None] * (N+1)
visited = [False] * (N+1)
adj = [list() for _ in range(N+1)]
q = Queue(N+1)

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    adj[node1].append(node2)
    adj[node2].append(node1)

init_tree()

for i in range(2, N+1):
    print(parent[i])

sys.stdin.close()


'''
0 1 2 3 4 5 6 7
0 6 4 6 1 3 1 4
'''