import sys
r, c = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline())) for _ in range(r)]
visited = [0] * 26
global length
length = 1
def dfs(x,y, cnt):
    global length
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[ord(board[x][y]) - 65] = 1
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < r and -1 < ny < c:
            n = ord(board[nx][ny]) - 65
            if not visited[n]:
                dfs(nx, ny, cnt)       
                length = max(length, cnt)
                visited[n] = 0
    return
dfs(0,0,1)
print(length)



        
