import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v+1)]

# 인접 리스트 튜플로 구현
for i in range(1, v+1):
    lst = list(map(int, input().split()))
    for j in range(1, len(lst)-1, 2):
        tree[lst[0]].append((lst[j], lst[j+1]))

cnt = 0
long = 0

def bfs(start):
    global cnt, long
    table = [0] * (v+1)
    q = deque([])
    q.append(start)

    while q:
        # 방문한 node를 꺼낸다 
        node = q.popleft()
        # 방문한 node와 인접한 node를 찾는다
        for i in range(len(tree[node])):
            # 인접한 node와 그 cost
            next, cost = tree[node][i]
            # 인접한 node가 start가 아닐 것 
            # 인접한 node가 방문한 node로 돌아가지 않을 것 
            if next != start and table[next] == 0:
                table[next] = table[node] + cost
                q.append(next)

    cnt = max(cnt, max(table))
    long = table.index(cnt)

bfs(1)
bfs(long)

print(cnt)
