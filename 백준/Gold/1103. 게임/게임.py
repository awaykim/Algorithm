
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
board = [list(map(str,sys.stdin.readline().strip())) for _ in range(n)] 
dp = [[0] * m for _ in range(n)]
visited = [[False]* m for _ in range(n)]
global ans
ans = 0

def dfs(x,y,c):
    global ans
    visited[x][y] = True
    dp[x][y] = c + 1
    ans = max(ans, dp[x][y])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  
    for i in range(4):
        nx, ny = x + dx[i]*int(board[x][y]), y + dy[i]*int(board[x][y])
        if -1 < nx < n and -1 < ny < m and board[nx][ny] != 'H':
            if dp[nx][ny] > c + 1: continue
            if visited[nx][ny]: 
                print(-1)
                exit()
            dfs(nx,ny,dp[x][y])
            visited[nx][ny] = False
    return 

dfs(0,0,0)
print(ans)