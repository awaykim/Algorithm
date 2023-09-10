from collections import deque
n, m = map(int, input().split())
graph = [[i] for i in range(n)]
for i in range(m):
    t, s = map(int, input().split())
    graph[t-1].append(s-1)
    graph[s-1].append(t-1)
global sum
sum = 0
visited = [0] * n
def bfs(v):
    global sum
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        p = q.popleft()
        for i in graph[p]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
    sum += 1
    return
for i in range(len(visited)):
    if visited[i] == 0:
        bfs(i)
print(sum)
