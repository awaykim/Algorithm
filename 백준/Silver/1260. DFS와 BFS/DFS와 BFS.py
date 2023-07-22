n, m, v = map(int, input().split())
graph = [[0 for i in range(n)] for j in range(n)]
dfs_visited = [False for i in range(n)]
bfs_visited = [False for i in range(n)]
dfs_vtx = []
bfs_vtx = []
q = []
for i in range(m):
    t, s = map(int, input().split())
    graph[t-1][s-1] = 1
    graph[s-1][t-1] = 1

def dfs(vtx):
    dfs_vtx.append(vtx+1)
    dfs_visited[vtx] = True
    for i in range(n):
        if graph[vtx][i] == 1 and dfs_visited[i] == False:
            dfs(i)
    return dfs_vtx

def bfs(vtx):
    bfs_visited[vtx] = True
    q.append(vtx)
    while q:
        a = q.pop(0)
        bfs_vtx.append(a+1)
        for i in range(n):
            if graph[a][i] == 1 and bfs_visited[i] == False:
                q.append(i)
                bfs_visited[i] = True
    return bfs_vtx

dfs_ans = dfs(v-1)
bfs_ans = bfs(v-1)

for i in dfs_ans:
    print(i, end=" ")
print()
for i in bfs_ans:
    print(i, end=" ")

