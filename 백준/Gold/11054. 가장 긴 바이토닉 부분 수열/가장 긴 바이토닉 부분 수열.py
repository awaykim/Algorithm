import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

def decrease(peak):
    if peak == n-1: return 0
    dp = [1] * n
    dp[peak] = 0
    
    for i in range(peak+1, n):
        if arr[i] == arr[peak]: 
            dp[i] = 0
            continue
        for j in range(peak, i):
            if arr[j] > arr[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp[peak:])

ascend = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and ascend[i] < ascend[j] + 1:
            ascend[i] = ascend[j] + 1

bitonic = [0] * n
for i in range(n):
    bitonic[i] = ascend[i] + decrease(i)

print(max(bitonic))