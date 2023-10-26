n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]
global cnt
cnt = 0
def find_row(x,y):
    global cnt
    for i in range(y, m):
        if board[x][i] == '-': 
            board[x][i] = 'v'
        else: 
            break
    cnt += 1
    return
def find_col(x,y):
    global cnt
    for i in range(x,n):
        if board[i][y] == '|':
            board[i][y] = 'v'
        else:
            break
    cnt += 1
    return
for i in range(n):
    for j in range(m):
        if board[i][j] == '-': 
            find_row(i,j)
        elif board[i][j] == '|':
            find_col(i,j)
        else: continue
print(cnt)
    
