# 2164 카드 
from collections import deque
n = int(input())
q = deque([x for x in range(1,n+1)])
flag = True
while True:
    if len(q) == 1: 
        print(q.pop())
        break
    if flag: 
        q.popleft()
        flag = not flag
    else:
        q.append(q.popleft())
        flag = not flag
