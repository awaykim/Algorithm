# 2644
from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[i] for i in range(n)]
for i in range(m):
    t, s = map(int, input().split())
    graph[t-1].append(s-1)
    graph[s-1].append(t-1)

def bfs(start, target):
    table = [-1] * n
    q = deque()
    q.append(start)
    table[start] = 0
    while q:
        s = q.popleft()
        for i in graph[s]:
            if i == s: continue
            if i == target: 
                print(table[s] + 1)
                exit()
            if table[i] == -1:
                q.append(i)
                table[i] = table[s] + 1
    print(-1)
    return
bfs(a-1,b-1)