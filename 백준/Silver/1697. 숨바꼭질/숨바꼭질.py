# 1697
from collections import deque
n, k = map(int, input().split())
MAX = 100001
dist = [0] * MAX
def bfs(x, y):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if x == y: 
            return dist[x]
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)
print(bfs(n, k))


