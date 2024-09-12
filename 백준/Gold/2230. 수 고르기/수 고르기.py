import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
start, end = 0, 1
ans = sys.maxsize
while start < n-1: 
    gap = arr[end] - arr[start] # 현재 두 수의 차이
    if gap == m: # 최선의 해를 찾으면 break
        ans = m
        break
    elif gap < m: # 유망하지 않음
        if end < n-1:
            end += 1 
        else:
            start += 1
    else: # 조건 통과
        ans = min(gap, ans)
        start += 1 # 더 작은 해답을 찾기 위해서
print(ans)