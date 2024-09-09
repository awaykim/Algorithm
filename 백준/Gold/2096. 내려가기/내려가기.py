max_dp = [0] * 3
min_dp = [0] * 3

n = int(input())

for i in range(n):
    new_max = [0] * 3
    new_min = [0] * 3
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0: 
            new_max[j] = a + max(max_dp[0], max_dp[1])
            new_min[j] = a + min(min_dp[0], min_dp[1])
        if j == 1:
            new_max[j] = b + max(max_dp[0], max_dp[1], max_dp[2])
            new_min[j] = b + min(min_dp[0], min_dp[1], min_dp[2])
        if j == 2:
            new_max[j] = c + max(max_dp[2], max_dp[1])
            new_min[j] = c + min(min_dp[2], min_dp[1])
    for j in range(3): 
        max_dp[j] = new_max[j]
        min_dp[j] = new_min[j]
    
print(max(max_dp), min(min_dp))