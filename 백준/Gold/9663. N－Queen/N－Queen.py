import sys
input = sys.stdin.readline

N = int(input())
row = [0] * N # row[i] = j: i행 j열에 퀸이 있다. 

def check(x): 
    for i in range(x):
        # 행 또는 열이 같은지 or 대각선에 존재하는지 
        # 대각선에 존재할 경우, 행의 차이와 열의 차이가 같다. 
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True
        
def dfs(x):
    global cnt
    # 마지막 행에 다다를 때 종료
    if x == N:
        cnt += 1
        return
    else:
        for i in range(N):
            # 현재 행에서 i열에 놓는다. 
            row[x] = i
            if check(x):
                # i열에 놓을 수 있을 경우 dfs한다. 
                dfs(x+1)


cnt = 0 
dfs(0)
print(cnt)