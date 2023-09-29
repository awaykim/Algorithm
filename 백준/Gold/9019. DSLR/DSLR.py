# 9019
from collections import deque
import sys
input = sys.stdin.readline
def D(num):
    num = int(num)
    return str((2 * num) % 10000)
def S(num):
    num = int(num)
    if num == 0: return '9999'
    else: return str(num - 1)
def L(num):
    if len(num) < 4: num = '0' * (4-len(num)) + num
    new = [num[1], num[2], num[3], num[0]]
    return "".join(new)
def R(num):
    if len(num) < 4: num = '0' * (4-len(num)) + num
    new = [num[3], num[0], num[1], num[2]]
    return "".join(new)
t = int(input())
for _ in range(t):
    graph = [''] * 10000
    a, b = map(str, input().split())
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        d, s, l, r = D(x), S(x), L(x), R(x)
        val = graph[int(x)]
        for i in range(4):
            if i == 0: c, p ='D', d
            elif i == 1: c, p= 'S', s
            elif i == 2: c, p = 'L', l
            else: c, p = 'R', r
            if graph[int(p)] == '' and x != p:
                q.append(p)
                graph[int(p)] = val + c
            if p == b: 
                print(graph[int(p)])
                q.clear()
                break
        