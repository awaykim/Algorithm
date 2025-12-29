import sys

N = int(sys.stdin.readline())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N):
  t = items[i][0]
  p = items[i][1]
  day = i + t
  if day <= N: dp[day] = max(dp[day], dp[i] + p)
  dp[i+1] = max(dp[i], dp[i+1]) 
print(max(dp))