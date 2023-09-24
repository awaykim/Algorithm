# 1707
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
K = int(input())
for i in range(K):
    V, E = map(int, input().split())
    graph = [set() for i in range(V)]
    for j in range(E):
        a, b = map(int, input().split())
        graph[a-1].add(b-1)
        graph[b-1].add(a-1)
    flag = False
    color = [-1] * V
    q = deque()
    while -1 in color:
        if flag: break
        idx = color.index(-1)
        q.append(idx)
        color[idx] = 0
        while q:
            if flag: break
            x = q.popleft()
            for k in graph[x]:
                if color[k] != -1:
                    if color[k] != color[x]: continue
                    else: 
                        flag = True
                        break
                else: 
                    q.append(k)
                    color[k] = 0 if color[x] else 1
    if flag: print('NO')
    else: print('YES')
    
         
