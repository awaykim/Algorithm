N = int(input())
arr = list(map(int, input().split()))
d = dict()

for a in arr:
  if a in d.keys():
    d[a] += 1
  else:
    d[a] = 1

def is_good(target: int):
  num = arr[target]
  d[num] -= 1
  flag = False
  for i in range(N):
    if flag: 
      break
    if i == target: 
      continue
    if num - arr[i] in d.keys():
      d[arr[i]] -= 1
      if d[num - arr[i]] > 0: 
        flag = True
      d[arr[i]] += 1
  d[num] += 1
  return flag

ans = 0

for i in range(N):
  if is_good(i):
    ans += 1

print(ans)