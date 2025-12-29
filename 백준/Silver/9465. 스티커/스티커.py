def solution(arr):
  dp = [[0] * N for _ in range(2)]
  for j in range(N):
    for i in range(2):
      if j:
        dp[i][j] = max(dp[1-i][j-1] + arr[i][j], dp[i][j-1])
      else:
        dp[i][j] = arr[i][j]
    
  return max(dp[1][N-1], dp[0][N-1])

T = int(input())

for _ in range(T):
  N = int(input())
  array = []
  for i in range(2):
    array.append(list(map(int, input().split())))
  print(solution(array))