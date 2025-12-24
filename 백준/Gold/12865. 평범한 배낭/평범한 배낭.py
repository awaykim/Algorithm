N, K = map(int, input().split())
items = []
for _ in range(N):
    items.append(list(map(int, input().split())))

# dp[i][w] -> 무게 w-kg에서 i번째 아이템까지 최대 가치
dp = [[0] * (K+1) for _ in range(N)]
# 초기화
# 0번째 아이템에서의 최대 가치
for i in range(items[0][0], K+1): 
    dp[0][i] = items[0][1]


# 1번째 아이템~N-1번째 아이템까지 
for i in range(1, N):
    w0 = items[i][0]
    v0 = items[i][1]

    for j in range(K+1):
      if w0 > j: 
          # 현재 무게에서의 최대 가치 = 이전과 동일
          dp[i][j] = dp[i-1][j]
      else:
          # 배낭에 넣지 않는다
          out_v = dp[i-1][j]
          # 배낭에 넣는다
          in_v = dp[i-1][j-w0] + v0
          dp[i][j] = max(out_v, in_v)
          

print(dp[N-1][K])