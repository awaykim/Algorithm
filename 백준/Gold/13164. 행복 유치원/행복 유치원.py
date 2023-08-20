# 13164
import sys
n, k = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
diff = []
for i in range(n - 1):
    diff.append(h[i + 1] - h[i])
diff.sort()
print(sum(diff[:n - k]))