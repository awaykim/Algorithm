import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heard = set()
seen = set()
for _ in range(n):
    heard.add(input().rstrip())
for _ in range(m):
    seen.add(input().rstrip())
ans = sorted(heard & seen)
print(len(ans))
for i in ans:
    print(i)