
def solution(n, array):
  def find(x):
    if parent[x] != x:
      parent[x] = find(parent[x])
    return parent[x]
  
  def union(a, b):
    a = find(a)
    b = find(b)

    if b > a:
      parent[b] = a
    else:
      parent[a] = b
    
  parent = [i for i in range(n)]
  for i in range(len(array)):
    if i == array[i]-1: continue
    union(i, array[i]-1)
  for i in range(n):
    parent[i] = find(i) 
  return len(set(parent))

t = int(input())

for _ in range(t):
  n = int(input())
  array = list(map(int, input().split()))
  print(solution(n, array))

