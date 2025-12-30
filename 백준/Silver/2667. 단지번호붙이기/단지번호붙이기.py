
N = int(input())
graph = []
for _ in range(N):
  graph.append(list(map(int, input())))

visited = [[0] * N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque

q = deque([])
total = 0
each = []
for i in range(N):
  for j in range(N):
    if not visited[i][j] and graph[i][j]:
      cur = 1 
      q.append((i,j))
      visited[i][j] = 1
      total += 1
      while q:
        x, y= q.popleft()
        for k in range(4):
          nx = x + dx[k]
          ny = y + dy[k]
          if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            cur += 1
            q.append((nx, ny))
      each.append(cur)

each.sort()

print(total)
for e in each:
  print(e)

