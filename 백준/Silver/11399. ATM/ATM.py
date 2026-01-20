ans = 0
P = []

N = int(input())
P = list(map(int, input().split()))

P.sort(key=lambda x : x)

for i in range(N):
  ans += sum(P[:i+1])

print(ans)