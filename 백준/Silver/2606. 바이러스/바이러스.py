N = int(input())
C = int(input())
graph = [[] for _ in range(N)] 
v = []
for i in range(C):
  n, m = map(int, input().split())
  graph[n-1].append(m-1)
  graph[m-1].append(n-1)

def find(c):
  if not c: return
  if c + 1 in v: return
  v.append(c+1)
  for i in graph[c]:
    find(i)

for i in graph[0]: 
  find(i)

print(len(v))