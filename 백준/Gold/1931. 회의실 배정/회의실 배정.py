ans = 0
t = []

N = int(input())
for _ in range(N):
  s, e = map(int, input().split())
  t.append((s, e))

t.sort(key=lambda x : (x[1], x[0]))
i = 0

for s, e in t:
  if i <= s:
    ans += 1
    i = e

print(ans)