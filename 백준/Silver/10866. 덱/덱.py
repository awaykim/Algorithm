# 10866
import sys
from collections import deque
n = int(sys.stdin.readline())

def solution(n):
    dq = deque()
    for i in range(n):
        command = list(map(str, sys.stdin.readline().split()))
        if command[0] == 'push_front':
            dq.appendleft(int(command[1]))
        elif command[0] == 'push_back':
            dq.append(int(command[1]))
        elif command[0] == 'pop_front':
            if dq: print(dq.popleft())
            else: print(-1)
        elif command[0] == 'pop_back':
            if dq: print(dq.pop())
            else: print(-1)
        elif command[0] == 'size':
            print(len(dq))
        elif command[0] == 'empty':
            if not dq: print(1)
            else: print(0)
        elif command[0] == 'front':
            if dq: print(dq[0])
            else: print(-1)
        else:
            if dq: print(dq[-1])
            else: print(-1)
    return

solution(n)