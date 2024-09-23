import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnts = dict()

for a in arr:
    if a not in cnts:
        cnts[a] = 1
    else:
        cnts[a] += 1

stack = []
ans = [-1] * n

for i in range(n):
    while stack and cnts[arr[stack[-1]]] < cnts[arr[i]]:
        
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)