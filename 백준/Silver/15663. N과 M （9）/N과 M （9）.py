ans = []
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
def dfs_9():
    if len(ans) == m:
        print(*ans)
        return 
    tmp = 0
    for i in range(n):
        if tmp == arr[i] or visited[i]: continue
        ans.append(arr[i])
        visited[i] = True
        tmp = arr[i]
        dfs_9()
        visited[i] = False
        ans.pop()
visited = [False] * n
dfs_9()