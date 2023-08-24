# 2178
import sys
from collections import deque
sys.setrecursionlimit(10**8)
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx == 0 and ny == 0: continue
            if -1 < nx < n and -1 < ny < m and graph[nx][ny] == 1: 
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1     
    return graph[n-1][m-1]
print(bfs(0,0))