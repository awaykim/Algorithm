N = int(input())
items = []
for _ in range(N):
  items.append(int(input()))

dp = [0] * N
dp[0] = items[0]

for i in range(1, N):
  d1 = dp[i-2] if i > 1 else 0
  d2 = dp[i-3] if i > 2 else 0
  c1 = d1 + items[i]
  c2 = d2 + items[i] + items[i-1]
  dp[i] = max(c1, c2, dp[i-1])

print(max(dp))