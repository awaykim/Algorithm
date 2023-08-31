import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
for i in range(n):
    c = int(sys.stdin.readline())
    if c not in coins:
        coins.append(c)
dp = [0] + [sys.maxsize] * k
for i in range(1, k+1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i-coin]+1, dp[i])
if dp[k] == sys.maxsize: print(-1)
else: print(dp[k])