import sys
input = sys.stdin.readline
n, m = map(int, input().split())
stack = []
def dfs():
    if len(stack) == m:
        print(' '.join(map(str,stack)))
        return
    for i in range(n):
        stack.append(i+1)
        dfs()
        stack.pop()
dfs()