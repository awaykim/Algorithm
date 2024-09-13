n = int(input())
arr = list(map(int, input().split()))

# 비내림차순
dp = [1] * n
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        dp[i] = dp[i-1] + 1
up = max(dp)
# 비오름차순
dp = [1] * n
arr = arr[::-1]
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        dp[i] = dp[i-1] + 1
down = max(dp)

print(max(up, down))