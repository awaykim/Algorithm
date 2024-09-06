from collections import deque

dx = [0,0,1,-1]
dy = [-1,1,0,0]

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
blind = [[False] * n for _ in range(n)]
counts = [0,0]

def bfs(a, b, arr, w):
    counts[w] += 1
    q = deque([(a, b)])
    arr[a][b] = True
    while q:
        x, y = q.popleft()
        color = graph[x][y]
        for i, j in zip(dx, dy):
            
            nx = x + i
            ny = y + j
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color and not arr[nx][ny]:
                arr[nx][ny] = True
                q.append((nx,ny))

for i in range(n):
     for j in range(n):
        if not visited[i][j]:
            bfs(i,j, visited, 0)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R': graph[i][j] = 'G'
for i in range(n):
     for j in range(n):
        if not blind[i][j]:
            bfs(i,j, blind,1)


print(*counts)