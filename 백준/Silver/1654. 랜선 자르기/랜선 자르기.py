K, N = map(int, input().split())
lines = []
for _ in range(K): 
  lines.append(int(input()))

right = sum(lines) // N or 1
left = max(lines) // N or 1
ans = 0 

while 0 < left <= right:
  a = 0
  mid = (left + right) // 2
  for l in lines:
    a += l // mid
  if a >= N:
    ans = mid
    left = mid+1
  else:
    right = mid-1

print(ans)