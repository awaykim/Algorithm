import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

table = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def dfs(node):
  
    visited[node] = True
    for next, cost in tree[node]:
        if not table[next] and not visited[next]:
            table[next] = table[node] + cost
            
            dfs(next)
            visited[next] = False
    
dfs(1)
long = table.index(max(table))

table = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dfs(long)
print(max(table))