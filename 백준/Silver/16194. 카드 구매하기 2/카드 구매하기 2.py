N = int(input())
P = list(map(int, input().split()))
P.insert(0,0)
def solution(arr):
    n = len(arr)
    dp = [0] * (n)
    dp[1] = arr[1]
    for i in range(2, n):
        r = i // 2
        tmp = []
        tmp.append(arr[i])
        for j in range(1, r+1):
            tmp.append(dp[j]+dp[i-j])
        # dp[i] = max(tmp)
        dp[i] = min(tmp)
    return(dp[n-1])

print(solution(P))