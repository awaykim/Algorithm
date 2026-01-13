# 1타일과 00타일로 만들 수 있는 크기가 N인 모든 수열 가짓수 % 15746
# dp[i] -> 크기 i일 떄의 가짓수 
# dp[i] = dp[i-2] + dp[i-1] 
N = int(input())
dp = [0 for _ in range(N+1)]
dp[1] = 1 # 1
if N > 1:
  dp[2] = dp[1] + 1 # 00, 11

if N > 2:
  for i in range(3, N+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[N])

