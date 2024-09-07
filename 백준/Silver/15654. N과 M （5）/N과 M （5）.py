n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
def dfs(depth):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(n):
        if arr[i] in ans: continue
        ans.append(arr[i])
        dfs(depth+1)
        ans.pop()
dfs(0)