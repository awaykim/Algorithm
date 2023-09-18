# 14863
import sys
n, k = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1 for _ in range(k+1)] for _ in range(n)]
dp[0][table[0][0]] = table[0][1]
dp[0][table[0][2]] = max(dp[0][table[0][2]], table[0][3])
for i in range(1, n):
    t_walk, v_walk, t_bike, v_bike = table[i]
    for j in range(k+1):
      if dp[i-1][j] != -1 and j+t_walk <= k:
         dp[i][j+t_walk] = max(dp[i][j+t_walk], dp[i-1][j] + v_walk)  
      if dp[i-1][j] != -1 and j+t_bike <= k:
         dp[i][j+t_bike] = max(dp[i][j+t_bike], dp[i-1][j] + v_bike)  
print(max(dp[n-1]))
