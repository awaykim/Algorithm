def dfs_1():
    if len(ans) == m:
        print(*ans)
        return 
    for i in range(1, n+1):
        if i in ans: continue
        ans.append(i)
        dfs_1()
        ans.pop()

ans = []
n, m = map(int, input().split())
dfs_1()