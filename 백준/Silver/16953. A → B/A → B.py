from collections import deque
A, B = map(int, input().split())
twice = lambda x: x*2
attch = lambda x: x*10+1
q = deque()
q.append((A,1))
while q:
    x, cnt = q.popleft()
    if x == B: 
        print(cnt)
        break
    cnt += 1
    if x < B:
        q.append((twice(x),cnt))
        q.append((attch(x),cnt))
if not q: print(-1)
