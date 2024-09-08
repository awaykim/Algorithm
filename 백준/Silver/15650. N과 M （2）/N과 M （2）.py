ans = []
n, m = map(int, input().split())
# dfs_1()

# 1~N 자연수 중 중복없이 M개를 고른 오름차순 수열
def dfs_2(start):
    if len(ans) == m:
        print(*ans)
        return 
    for i in range(start, n+1):
        if i in ans: continue
        ans.append(i)
        dfs_2(i)
        ans.pop()

dfs_2(1)