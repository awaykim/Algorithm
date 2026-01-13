N, K = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(int(input()))

remain = K
answer = 0

for a in arr[::-1]:
  if remain < 0 or remain < a: continue
  answer += remain // a
  remain %= a 

print(answer)