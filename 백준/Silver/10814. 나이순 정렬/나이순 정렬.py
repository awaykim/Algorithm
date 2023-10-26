n = int(input())
members = [input().split() for _ in range(n)]
members = sorted(members, key=lambda x: int(x[0]))
for i in range(n):
    print(*members[i])