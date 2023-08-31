import sys
n = int(sys.stdin.readline())
dp = [0] + [(i-1) for i in range(1, n+1)]
for i in range(2, len(dp)):
    sub_res = [sys.maxsize] * 3
    if i % 3 == 0: sub_res[0] = dp[i//3] + 1
    if i % 2 == 0 : sub_res[1] = dp[i//2] + 1
    sub_res[2] = dp[i-1] + 1
    dp[i] = min(sub_res)
print(dp[n])