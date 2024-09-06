# 14940 쉬운 최단거리
from collections import deque

dx = [0,0,1,-1]
dy = [-1,1,0,0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

def bfs(a,b):
    q = deque([(a,b)])
    visited[a][b] = 0
    while q:
        x, y = q.popleft()
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: 
            bfs(i, j)
        if graph[i][j] == 0:
            visited[i][j] = 0

for i in range(n):
    print(*visited[i])
