import sys
from collections import deque
def change(n,a,b):
    nn = list(str(n))
    if nn[a] != nn[b]: nn[a], nn[b] = nn[b], nn[a]
    return nn
n, k = map(int, sys.stdin.readline().split())
ans = 0
q = deque()
q.append((n,0))
while q:
    n, cnt = q.popleft()
    for i in range(len(str(n))-1):
        for j in range(i+1, len(str(n))): 
            nn = change(n, i, j)
            if nn[0] == '0': continue
            num = int(''.join(map(str, nn)))
            if (num, cnt+1) in q: continue
            if cnt == k - 1:
                ans = max(ans, num)
            else:
                q.append((num, cnt+1))
if ans: print(ans)
else: print(-1)




