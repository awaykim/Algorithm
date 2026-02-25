import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[1 if i==j else 0 for j in range(N)] for i in range(N)]

for i in range(1, N):
  for start in range(N-i):
    end = start + i
    if nums[start] == nums[end]:
      if start+1 == end:
        dp[start][end] = 1
      elif dp[start+1][end-1] == 1:
        dp[start][end] = 1

M = int(input())
for _ in range(M):
  s, e = map(int, input().split())
  print(dp[s-1][e-1])