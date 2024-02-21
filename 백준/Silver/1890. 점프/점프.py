n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        val = board[i][j]
        if i + val < n:
            dp[i+val][j] += dp[i][j]
        if j + val < n:
            dp[i][j+val] += dp[i][j]
print(dp[n-1][n-1])
