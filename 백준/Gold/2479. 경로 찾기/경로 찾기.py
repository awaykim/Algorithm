import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
codes = []
for i in range(N):
    codes.append(list(map(int, sys.stdin.readline().strip())))
A, B = map(int, sys.stdin.readline().split())
visited = [False for _ in range(N)]
ans = []
def isHamming(v, w):
    cnt = 0
    for i in range(len(v)):
        if v[i] != w[i]: cnt +=1
    if cnt == 1: return True
    else: return False

def bfs(a, b):
    q = deque()
    q.append([a])
    visited[a-1] = True
    while q:
        path = q.popleft()
        node = path[-1]
        if node == b: 
            return path
        for i in range(len(codes)):
            if isHamming(codes[node-1], codes[i]) and not visited[i]: 
                new_path = path[:]
                new_path.append(i+1)
                q.append(new_path)
                visited[i] = True  
    return []
ans = bfs(A,B)
if ans: print(*ans)
else: print(-1)