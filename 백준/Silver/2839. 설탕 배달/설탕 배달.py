n = int(input())

dp = [0] * 5001
dp[3] = dp[5] = 1

for i in range(3, len(dp)):
    if dp[i-3] and dp[i-5]:
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    elif dp[i-3] and not dp[i-5]:
        dp[i] = dp[i-3] + 1
    elif dp[i-5]:
        dp[i] = dp[i-5] + 1

    if i == n: 
        if dp[n] == 0: print(-1)
        else: print(dp[n])
        break
