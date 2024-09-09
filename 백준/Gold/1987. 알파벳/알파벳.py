import sys
input = sys.stdin.readline 
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [False for _ in range(26)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = ans = 0
visited[ord(board[0][0])-ord('A')] = True

def dfs(x, y):
    global cnt, ans
    cnt += 1
    for i, j in zip(dx, dy):
        nx, ny = x+i, y+j
        if 0 <= nx < r and 0 <= ny < c and not visited[ord(board[nx][ny])-ord('A')]:
            visited[ord(board[nx][ny])-ord('A')] = True
            dfs(nx, ny)
            visited[ord(board[nx][ny])-ord('A')] = False
    ans = max(ans, cnt)
    cnt -= 1
    return
                
dfs(0,0)
print(ans)
