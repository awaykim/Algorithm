import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
indegree = [0] * (n+1) # 진입차수
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1  

def topology_sort():
    res = []
    q = deque()
    for i in range(1, n+1): 
        if not indegree[i]: q.append(i)
    while q:
        x = q.popleft()
        res.append(x)
        for i in graph[x]:
            indegree[i] -= 1
            if not indegree[i]: q.append(i)
    for r in res:
        print(r, end=' ')

topology_sort()


