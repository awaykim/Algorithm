t = int(input())
dp = [1] * 11
for i in range(2, 11):
    if i < 4: dp[i] = sum(dp[0:i])
    else: dp[i] = sum(dp[i-3:i])
for _ in range(t):
    n = int(input())
    print(dp[n])