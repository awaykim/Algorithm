import sys
from collections import deque

input = sys.stdin.readline
q = deque()

n = int(input())
graph = [0] + [set(list(map(int, input().split()))[:-1]) for _ in range(n)]
time = [-1 for i in range(n+1)]

m = int(input())
rumor = set(map(int, input().split()))
for i in rumor:
    q.append(i)
    time[i] = 0

while q:
    x = q.popleft()
    rumor.add(x)
    nset = graph[x] - rumor
    for v in nset:
        if time[v] > -1: continue
        if len(graph[v] & rumor) >= len(graph[v]) / 2:
            q.append(v)
            time[v] = time[x] + 1

print(*time[1:])