import sys
n = int(input())
snows = list(map(int, input().split()))
snows.sort()
ans = sys.maxsize
for i in range(n-1):
    for j in range(i+1, n):
        anna = snows[i] + snows[j] 
        start, end = 0, n-1
        while start < end:
            if start == i or start == j: 
                start += 1
                continue
            if end == j or end == i: 
                end -= 1
                continue
            elsa = snows[start] + snows[end]
            if elsa > anna: 
                end -= 1
            elif elsa < anna: 
                start += 1
            else:
                print(0)
                exit(0)
            ans = min(ans, abs(elsa-anna))
print(ans)