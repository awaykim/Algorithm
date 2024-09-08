ans = []
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

def dfs_7():
    if len(ans) == m:
        print(*ans)
        return 
    for i in range(n):
        ans.append(arr[i])
        dfs_7()
        ans.pop()
dfs_7()