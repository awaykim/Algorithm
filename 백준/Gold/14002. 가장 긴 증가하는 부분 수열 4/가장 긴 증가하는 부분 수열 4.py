# 14002
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
k = max(dp)
print(k)
idx = dp.index(k)
l = idx
ans = [arr[idx]]
for i in range(idx - 1, -1, -1):
    if dp[i] == k - 1 and arr[i] < arr[l]:
        ans.append(arr[i])
        k -=1
        l = i
print(*ans[::-1])
