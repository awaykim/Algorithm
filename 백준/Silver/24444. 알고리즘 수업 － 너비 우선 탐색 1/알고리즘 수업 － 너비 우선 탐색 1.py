from collections import deque

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n):
    graph[i].sort()
q = deque([r])
cnt = visited[r] = 1
while q:
    x = q.popleft()
    for i in graph[x]:
        if not visited[i]:
            cnt += 1
            q.append(i)
            visited[i] = cnt
for i in range(1, n+1):
    print(visited[i])