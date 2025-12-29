N, K = map(int, input().split())
coins = []
for _ in range(N):
  coins.append(int(input()))

dp = [0 for _ in range(K+1)]

for coin in coins:
  for k in range(1, K+1):
    if k == coin:
      dp[k] += 1
    if k > coin:
      dp[k] += dp[k-coin]

print(dp[K])