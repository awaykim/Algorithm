def up_stair():
    N = int(input())
    score = [int(input()) for _ in range(N)]
    dp = [0 for _ in range(N)]
    if N < 3: print(sum(score))
    else:
        dp[0] = score[0]
        dp[1] = score[0] + score[1]
        for i in range(2, N):
            dp[i] = max(dp[i-3]+score[i-1]+score[i], dp[i-2]+score[i])
        print(dp[-1])

up_stair()