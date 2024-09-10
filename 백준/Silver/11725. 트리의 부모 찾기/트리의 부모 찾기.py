import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
parents = [0 for _ in range(n+1)]
parents[1] = -1
def dfs(i):
    for node in tree[i]:
        if parents[node]: continue
        parents[node] = i 
        dfs(node)
dfs(1)
for i in range(2, n+1):
    print(parents[i])
