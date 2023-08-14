# 1446

import sys
n, d = map(int, sys.stdin.readline().split())
short_cuts = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solution(d, arr):
    arr.sort(key=lambda x: (x[1], x[0]))
    
    dp = [i for i in range(d + 1)]
    for a in arr:
        start, end, dist = a[0], a[1], a[2]
        if end > d: continue
        if dp[start] + dist + d - end < dp[d]: 
            dp[end] = dp[start] + dist
            for i in range(end, d + 1):
                dp[i] = dp[end] + i - end
            # print('!', start, end, dp[end], dp[d])
      
    print(dp[d])
    return
        
        
solution(d, short_cuts)