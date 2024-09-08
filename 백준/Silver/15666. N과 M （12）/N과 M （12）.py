ans = []
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
def dfs_12(start):
    if len(ans) == m:
        print(*ans)
        return
    tmp = 0
    for i in range(start,n):
        if tmp == arr[i]: continue
        ans.append(arr[i])
        tmp = arr[i]
        dfs_12(i)
        ans.pop()
dfs_12(0)