n, m = map(int, input().split())
ans = []
def dfs(start):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(start, n+1):
        ans.append(i)
        dfs(i)
        ans.pop()
dfs(1)